from faker import Faker
import csv
import random
from datetime import datetime, timedelta


fake = Faker()
EMPLEADOS_LIMIT = 10


def diferencia_dias(fecha1, fecha2):
    return (fecha1 - fecha2).days

def create_all_employis(sucursales):

    print('Creando usuarios....\n\n')

    for x in range(0, EMPLEADOS_LIMIT):
        random_sucursal = sucursales[random.randint(0, len(sucursales)-1)]
        fecha_de_ingreso = timezone.make_aware(
            fake.date_time(), timezone.get_current_timezone()
        )

        user = User.objects.create(
            email=fake.email(), password=fake.password(), first_name=fake.first_name(), 
            last_name=fake.last_name(), username=fake.name(), date_joined=fecha_de_ingreso
        )

        personal = Personal.objects.create(
            usuario=user, sucursal=random_sucursal, phone_number=fake.phone_number()
        )

        print(f'Usuario {user.first_name}, creado')

        if random.randint(0, 10) == 0:
            AltaPersonal.objects.create(
                personal=personal, sucursal=random_sucursal, fecha=fecha_de_ingreso
            )
            BajaPersonal.objects.create(
                personal=personal, sucursal=random_sucursal, fecha=timezone.now(),
                motivo = random.randint(0, 2) == 0 if 'abandono' else 'voluntaria'
            )
            personal.is_active = False
            personal.save()

            print(f'Alta y luego baja del usuario')
        else:
            AltaPersonal.objects.create(
                personal=personal, sucursal=random_sucursal, fecha=fecha_de_ingreso
            )
            print(f'Alta del usuario')
        
        dias_trabajados = diferencia_dias(timezone.now(), fecha_de_ingreso)
        
        if dias_trabajados > 30:
            dias_trabajados = 30

        aux_date = fecha_de_ingreso

        print('Creando las listas de asistencias...')
        for x in range(1, dias_trabajados):
            PaseLista.objects.create(
                personal=personal,
                asistio= random.randint(0, 10) == 0 if False else True,
                fecha=aux_date
            )
            aux_date = aux_date + timedelta(days=1)

def createSucursales():
    SUCURSALES = [
        {
            'coords': [18.003511574398956, -92.98362654472939],
            'name': 'Tabasco'
        },
        {
            'coords': [22.26548427983087, -97.87491935447295],
            'name': 'Tamaulipas 1'
        },
        {
            'coords': [18.681406437828855, -91.74897796829059],
            'name': 'Campeche'
        },
        {
            'coords': [20.538383292017386, -97.39254363418814],
            'name': 'Veracruz 1'
        },
        {
            'coords': [19.17227844429708, -96.22513406341882],
            'name': 'Veracruz 2'
        },
        {
            'coords': [26.0842084874065, -98.31444467156702],
            'name': 'Tamaulipas 2'
        }
    ]

    REDES = ['Facebook', 'Instagram', 'Tiktok']

    print('Creando las sucursales y los datos de las redes')
    sucursales = []
    for x in SUCURSALES:
        suc = Sucursal.objects.create(
            nombre=x['name'], latitud=x['coords'][0], longitud=x['coords'][1]
        )
        sucursales.append(suc)

        date = timezone.make_aware(fake.date_time(), timezone.get_current_timezone())

        Redes.objects.create(
            sucursal=suc, red_name=REDES[random.randint(0, len(REDES)-1)],
            fecha=date, cantidad=random.randint(30, 200)
        )
    
    return sucursales


def createQuestionario():
    questionario = Questionario.objects.create(nombre='Questionario 360°')
    print(f'Creando el questionari 360°')
    with open('initialData/preguntas360.csv', encoding='utf-8') as csv_file:

        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        print('Creando las preguntas y las posibles respuestas con su porcentaje correspondiente')
        for row in csv_reader:
            if line_count != 0:
                pregunta = Preguntas.objects.create(
                    questionario=questionario, pregunta=row[0]
                )
                total = 3
                if (len(row[4])>0):
                    total = 4
                Respuestas.objects.create(
                    questionario=questionario, respuesta=row[1], 
                    porcentaje=100/total, pregunta=pregunta
                )
                Respuestas.objects.create(
                    questionario=questionario, respuesta=row[2], 
                    porcentaje=(100/total)*2, pregunta=pregunta
                )
                Respuestas.objects.create(
                    questionario=questionario, respuesta=row[3], 
                    porcentaje=(100/total)*3, pregunta=pregunta
                )

                if total == 4:
                    Respuestas.objects.create(
                        questionario=questionario, respuesta=row[3], 
                        porcentaje=100, pregunta=pregunta
                    )   
            line_count += 1


def eachUserResolveQuestionario():
    all_personal = Personal.objects.all()
    questionario = Questionario.objects.all()[0]
    preguntas = Preguntas.objects.filter(questionario=questionario)

    print('Haciendo que los usuarios falsos resuelvan sus examenes')
    print(questionario)
    print(preguntas)
    for x in all_personal:
        resultado = 0
        valor_pregunta = 100 / len(preguntas)
        for pregunta in preguntas:
            respuestas = Respuestas.objects.filter(pregunta=pregunta)
            user_response = respuestas[random.randint(0, len(respuestas)-1)]
            resultado += (valor_pregunta / 100) * user_response.porcentaje
            UserRespuestas.objects.create(
                questionario=questionario,
                respuesta=user_response,
                personal=x
            )
        print(f'El usuario {x.usuario.first_name} obtuvo un puntuaje de {resultado}')

# exec(open('initialData/script.py').read())
def main():
    # Crea las sucursales y los registros de redes sociales
    sucursales = createSucursales()

    # Crea todos los usuarios, empleados, listas, altas y bajas
    create_all_employis(sucursales)

    # Crea el unico questionario que existe
    createQuestionario()

    # Hace que todos los usuarios respondan una encuesta
    eachUserResolveQuestionario()