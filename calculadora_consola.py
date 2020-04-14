# Calculadora que funciona en consola
# Funciona con numeros reales

options = ['Sumar', 'Restar', 'Multiplicar', 'Dividir', 'Salir']


def mostrar_menu():
    print('***CALCULADORA***')
    for i in range(len(options)):
        print(f'{i + 1}. {options[i]}')


def pedir_numero(mensaje):
    option = int(input(mensaje))
    return option


# Main Program
sw = True
while sw:
    mostrar_menu()
    option = pedir_numero('Que operacion deseas realizar\n')
    if 0 < option < 5:
        num1 = pedir_numero('Ingrese el primer numero\n')
        num2 = pedir_numero('Ingrese el segundo numero\n')
        if option == 1:
            res = num1 + num2
        elif option == 2:
            res = num1 - num2
        elif option == 3:
            res = num1 * num2
        elif option == 4:
            res = num1 / num2
        print(f'El resultado es {round(res,2)}')
    elif option == 5:
        sw = 0
    else:
        print('Opcion Incorrecta')
print('Gracias por usar la calculadora')
