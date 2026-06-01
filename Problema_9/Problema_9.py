# Problema 9: Coeficientes multinomiales
#
# Este programa calcula el número de formas distintas
# de ordenar elementos cuando algunos de ellos se repiten.
#
# Puede utilizarse de dos maneras:
# 1. Ingresando una palabra con letras repetidas.
# 2. Ingresando directamente las cantidades repetidas
#    de cada tipo de elemento.
#
# Se utilizo el teorema multinomial

# Mensajes de presentación del programa
print("Coeficientes multinomiales y palabras con letras repetidas")
print("El siguiente programa busca realizar combinaciones con repetición. \nDebe ingresar una palabra o una cadena de numeros con las cantidades repetidas de cada elemento. \n")

# Menú principal
print("Elegir una opción:")
print("1. Ingresar palabra")
print("2. Ingresar cadena de numeros")

# Función recursiva para calcular el factorial de un número
def factorial(numero):
        if numero == 0:
            return 1
        else:
            return numero * factorial(numero - 1)

# Variables auxiliares
#
# suma:
# almacena el número total de elementos (n)
#
# denominador:
# almacena el producto de los factoriales
# de las repeticiones (n1!·n2!·...·nr!)
denominador = 1
suma = 0

try:

    # Lectura de la opción seleccionada por el usuario
    opcion = int(input("Digite una opción: "))

    # Validar que la opción pertenezca al menú
    if opcion < 1 or opcion > 2:
        raise ValueError("La entrada no pertenece al rango solicitado")

    match opcion:

        # Caso 1:
        # El usuario ingresa una palabra
        case 1:

            palabra = input("Ingrese una palabra: ")

            # Verificar que la palabra solo contenga letras
            if not palabra.isalpha():
                raise ValueError("La entrada contiene números o caracteres no válidos.")

            # Analizar cada letra distinta de la palabra
            while(len(palabra) != 0):

                # Convertir a minúsculas para considerar
                # iguales las letras mayúsculas y minúsculas
                palabra = palabra.lower()

                # Contar cuántas veces aparece la primera letra
                letra = palabra.count(palabra[0])

                # Eliminar todas las apariciones de esa letra
                # para evitar volver a contarlas
                palabra = palabra.replace(palabra[0], "")

                # Acumular el número total de letras
                suma += letra

                # Multiplicar por el factorial de la cantidad repetida
                denominador *= factorial(letra)

        # Caso 2:
        # El usuario ingresa directamente las cantidades
        # de elementos repetidos
        case 2:

            arreglo = input("Ingrese los números separados con comas: ")

            # Separar la cadena utilizando las comas
            letras_repetidos = arreglo.split(",")

            # Procesar cada cantidad ingresada
            for letra in letras_repetidos:

                # Convertir la entrada a entero
                letra = int(letra)

                # Verificar que la cantidad sea positiva
                if letra <= 0:
                    raise ValueError("La entrada contiene números no válidos.")

                # Acumular el número total de elementos
                suma += letra

                # Multiplicar por el factorial correspondiente
                denominador *= factorial(letra)

    # Aplicar la fórmula multinomial
    resultado = factorial(suma) // denominador

    # Mostrar el resultado final
    print("El resultado de las combinaciones posibles es " + str(resultado))

# Manejo de errores de entrada
except ValueError as error:
    print("Error de entrada: " + str(error))

except ValueError:
    print("Entrada no valida")
