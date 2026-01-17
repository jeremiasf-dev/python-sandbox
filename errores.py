try:
    value = int(input('Ingresa un número natural: '))
    print('El recíproco de', value, 'es', 1/value)        
except ValueError:
    print('No se que hacer con ' , value)    
except ZeroDivisionError:
    print('La división entre cero no está permitida en nuestro Universo.')    
except TypeError:
    print("No papi numero natural, no letras okk")
except:
    print('Ha sucedido algo extraño, ¡lo siento!')
