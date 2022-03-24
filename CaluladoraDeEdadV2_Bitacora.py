from datetime import date
from operator import truediv
import sys, os, time, logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.INFO,
                    filename='app.log',
                    filemode='a')


def calcular_edad(fecha_nacimiento):
    fecha_actual = date.today()
    resultado = fecha_actual.year - fecha_nacimiento.year
    resultado -= ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return resultado

if __name__ == '__main__':
    while True:
        try:
            print('Recuerda introducir tus datos correctos \n')
            year = int(input('¿En que año naciste?'))
            month = int(input('¿En que mes naciste?'))
            day = int(input('¿En que dia naciste?'))
            break;
        except ValueError as err: 
            print('Woops, estas ingresando los datos erroneos')
            print('Debes recordar que solo se reciben numeros')
            print('Vamos a intentarlo de nuevo')
            logging.exception('No se introdujeron fechas correctas', stack_info=True)
            time.sleep(5)
            os.system("clear")
    try:    
        DateCon = date(year, month, day)
        verificacion = calcular_edad(DateCon)
        if 1 > verificacion:
            print ("¿Estas seguro de que ya naciste? ")
        else:
            print (f"Tu edad es de {verificacion} años")
    except ValueError as err:
        print('Hmmm al parecer estas ingresando datos no elegibles \n')
        print('Año No Viciesto')
        print('Los datos se encuentran fuera del rango de Mes o Dias')
        print('Verificalo e intentalo')
        print('Tus datos son los siguientes: \n')
        print(f'Año: {year}, Mes: {month}, Dia: {day}')
        logging.exception('Los datos se encuentran fuera del rango de Mes o Dias', stack_info=True)

        
        exit()


        


        
