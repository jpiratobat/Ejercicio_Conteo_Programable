# Problema 7: Sistema de conteo de contraseñas
#
# Este programa calcula la cantidad de contraseñas posibles
# bajo diferentes restricciones de construcción.
#
# Restricciones disponibles:
# - Permitir o no repeición de caracteres.
# - Exigir al menos un dígito.
# - Exigir al menos una letra mayúscula.
# - Exigir al menos un símbolo especial.
#
# Para los casos con múltiples restricciones se utiliza
# el Principio de Inclusión-Exclusión.

# Mensajes de presentación del programa
print("Sistema de conteo de contraseñas")
print("El siguiente programa busca realizar combinaciones con repetición. \n"
        "Letras en mayúsculas: A a Z (26 caracteres)\n"
        "Letras en minúsculas: a a z (26 caracteres)\n"
        "Números: 0 a 9 (10 caracteres)\n"
        "Símbolos: (espacio) ! \" # $ % & \' ( ) * + , - . / : ; < = > ? @ [ \\ ] ** _` { | } ~ (33 caracteres)\n")

# Función recursiva para calcular el factorial de un número
def factorial(numero):
        if numero == 0:
            return 1
        else:
            return numero * factorial(numero - 1)

# Función para calcular permutaciones sin repetición
#
# Fórmula:
# P(n,r) = n! / (n-r)!
#
# n = número total de caracteres disponibles
# r = longitud de la contraseña
def permutacion(n,r):

    # Validar que existan suficientes caracteres
    # para formar la contraseña sin repetición
    if(n < r):
        print("El numero de combinaciones no es posible de realizar. Los elementos son insuficientes para la contraseña")
        return 0

    else:
        return factorial(n)//factorial(n-r)

# Variable utilizada para almacenar las opciones elegidas
#
# Se usa una máscara binaria:
#
# Repetición              = 1
# Dígito obligatorio      = 2
# Mayúscula obligatoria   = 4
# Símbolo obligatorio     = 8
#
# Esto genera 16 combinaciones posibles:
# desde 0 hasta 15.
menu=0

try:

    # Lectura del tamaño del alfabeto
    alfabeto= int(input("Tamaño del alfabeto: "))

    # Validar que el alfabeto esté dentro del rango permitido
    if alfabeto>26 or alfabeto<=0:
        raise ValueError("El abecedario [EN] solo contiene 26 letras")

    # Lectura de la longitud de la contraseña
    longitud= int(input("Tamaño máximo de la contraseña: "))

    # Validar longitud positiva
    if longitud<=0:
        raise ValueError("El tamaño de la contraseña no puede ser negativo")

    # Preguntar si se permite la repetición
    opcion = input("¿Se permite la repetición? S/N: ")

    if opcion.upper()=="S":
        menu+=1
    elif opcion.upper()=="N":
        pass
    else:
        raise ValueError("El caracter usado no fue el solicitado")

    # Preguntar si se exige al menos un dígito
    opcion = input("¿Debe contener al menos un digito? S/N: ")

    if opcion.upper()=="S":
        menu+=2
    elif opcion.upper()=="N":
        pass
    else:
        raise ValueError("El caracter usado no fue el solicitado")

    # Preguntar si se exige al menos una mayúscula
    opcion = input("¿Debe contener al menos una letra mayúscula? S/N: ")

    if opcion.upper()=="S":
        menu+=4
    elif opcion.upper()=="N":
        pass
    else:
        raise ValueError("El caracter usado no fue el solicitado")

    # Preguntar si se exige al menos un símbolo especial
    opcion = input("¿Debe contener al menos un símbolo especial? S/N: ")

    if opcion.upper()=="S":
        menu+=8
    elif opcion.upper()=="N":
        pass
    else:
        raise ValueError("El caracter usado no fue el solicitado")

    # Selección de la fórmula correspondiente
    # según las restricciones elegidas
    match menu:

        # Caso 0:
        # Sin repetición y sin restricciones adicionales
        case 0:
            resultado = permutacion(2*alfabeto + 10 + 33, longitud)

        # Caso 1:
        # Con repetición y sin restricciones adicionales
        case 1:
            resultado = ((2*alfabeto + 10 + 33)**longitud)

        # Caso 2:
        # Sin repetición y al menos un dígito
        case 2:
            resultado = (
                permutacion(2*alfabeto + 10 + 33, longitud)
                - permutacion(2*alfabeto + 33, longitud)
            )

        # Caso 3:
        # Con repetición y al menos un dígito
        case 3:
            resultado = (
                ((2*alfabeto + 10 + 33)**longitud)
                - ((2*alfabeto + 33)**longitud)
            )

        # Caso 4:
        # Sin repetición y al menos una mayúscula
        case 4:
            resultado = (
                permutacion(2*alfabeto + 10 + 33, longitud)
                - permutacion(alfabeto + 10 + 33, longitud)
            )

        # Caso 5:
        # Con repetición y al menos una mayúscula
        case 5:
            resultado = (
                ((2*alfabeto + 10 + 33)**longitud)
                - ((alfabeto + 10 + 33)**longitud)
            )

        # Caso 6:
        # Sin repetición
        # Al menos un dígito y una mayúscula
        # Inclusión-Exclusión para dos restricciones
        case 6:
            resultado = (
                permutacion(2*alfabeto + 10 + 33, longitud)
                - permutacion(2*alfabeto + 33, longitud)
                - permutacion(alfabeto + 10 + 33, longitud)
                + permutacion(alfabeto + 33, longitud)
            )

        # Caso 7:
        # Con repetición
        # Al menos un dígito y una mayúscula
        case 7:
            resultado = (
                ((2*alfabeto + 10 + 33)**longitud)
                - ((2*alfabeto + 33)**longitud)
                - ((alfabeto + 10 + 33)**longitud)
                + ((alfabeto + 33)**longitud)
            )

        # Caso 8:
        # Sin repetición y al menos un símbolo
        case 8:
            resultado = (
                permutacion(2*alfabeto + 10 + 33, longitud)
                - permutacion(2*alfabeto + 10, longitud)
            )

        # Caso 9:
        # Con repetición y al menos un símbolo
        case 9:
            resultado = (
                ((2*alfabeto + 10 + 33)**longitud)
                - ((2*alfabeto + 10)**longitud)
            )

        # Caso 10:
        # Sin repetición
        # Al menos un dígito y un símbolo
        case 10:
            resultado = (
                permutacion(2*alfabeto + 10 + 33, longitud)
                - permutacion(2*alfabeto + 10, longitud)
                - permutacion(2*alfabeto + 33, longitud)
                + permutacion(2*alfabeto, longitud)
            )

        # Caso 11:
        # Con repetición
        # Al menos un dígito y un símbolo
        case 11:
            resultado = (
                ((2*alfabeto + 10 + 33)**longitud)
                - ((2*alfabeto + 10)**longitud)
                - ((2*alfabeto + 33)**longitud)
                + ((2*alfabeto)**longitud)
            )

        # Caso 12:
        # Sin repetición
        # Al menos una mayúscula y un símbolo
        case 12:
            resultado = (
                permutacion(2*alfabeto + 10 + 33, longitud)
                - permutacion(2*alfabeto + 10, longitud)
                - permutacion(alfabeto + 10 + 33, longitud)
                + permutacion(alfabeto + 10, longitud)
            )

        # Caso 13:
        # Con repetición
        # Al menos una mayúscula y un símbolo
        case 13:
            resultado = (
                ((2*alfabeto + 10 + 33)**longitud)
                - ((alfabeto + 10 + 33)**longitud)
                - ((2*alfabeto + 10)**longitud)
                + ((alfabeto + 10)**longitud)
            )

        # Caso 14:
        # Sin repetición
        # Al menos un dígito, una mayúscula y un símbolo
        # Inclusión-Exclusión para tres restricciones
        case 14:
            resultado = (
                permutacion(2*alfabeto + 10 + 33, longitud)
                - permutacion(alfabeto + 10 + 33, longitud)
                - permutacion(2*alfabeto + 10, longitud)
                - permutacion(2*alfabeto + 33, longitud)
                + permutacion(alfabeto + 10, longitud)
                + permutacion(2*alfabeto, longitud)
                + permutacion(alfabeto + 33, longitud)
                - permutacion(alfabeto, longitud)
            )

        # Caso 15:
        # Con repetición
        # Al menos un dígito, una mayúscula y un símbolo
        # Inclusión-Exclusión para tres restricciones
        case 15:
            resultado = (
                ((2*alfabeto + 10 + 33)**longitud)
                - ((2*alfabeto + 33)**longitud)
                - ((2*alfabeto + 10)**longitud)
                - ((alfabeto + 10 + 33)**longitud)
                + ((alfabeto + 10)**longitud)
                + ((alfabeto + 33)**longitud)
                + ((2*alfabeto)**longitud)
                - ((alfabeto)**longitud)
            )

    # Mostrar el resultado obtenido
    print("El resultado de combinaciones es: " + str(resultado))

# Manejo de errores de entrada
except ValueError as error:
    print("Error de entrada: " + str(error))

except ValueError:
    print("Entrada no valida")
