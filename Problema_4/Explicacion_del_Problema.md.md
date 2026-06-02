## Problema 4: Sistema de conteo de contraseñas
Este programa calcula la cantidad de contraseñas posibles a partir de un conjunto de caracteres definido por:
1. Letras en mayúsculas: A a Z (26 caracteres) - **_Variable_**
2. Letras en minúsculas: a a z (26 caracteres) - **_Variable_**
3. Números: 0 a 9 (10 caracteres)
4. Símbolos: (espacio) ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _` { | } ~ (33 caracteres)

Además, las contraseñas pueden estar sujetas a las siguientes restricciones:
¿Al menos con una letra mayúscula?
¿Al menos con un número?
¿Al menos con un símbolo?

Para calcular el número de contraseñas que satisfacen estas condiciones se utiliza el Principio de Inclusión-Exclusión, junto con fórmulas de permutaciones y conteo con repetición.

#### Fórmulas Utilizadas
Permutación (Elementos sin repetir)

$$
_{n}P_{r} = \frac{n!}{(n-r)!}
$$

Potencia (Elementos repetidos)

$$
	n^r
$$

Principio de inclusión-exclusión

$$
 \text{ 1 restricción}= |U| - |A|
$$

$$
 \text{ 2 restricción}= |U| - |A| - |B| + |A\cap B|
$$

$$
 \text{ 3 restricción}= |U| - |A| - |B| - |C| + |A\cap B| + |B \cap C| + |A \cap C| - |A \cap B \cap C|
$$

### Algoritmo 
1.   Leer el tamaño del alfabeto y la longitud máxima de la contraseña.
2.  Validar que los valores ingresados sean correctos.
3. Preguntar si:
    -   Se permite repetición de caracteres.
    -   La contraseña debe contener al menos un dígito.
    -   La contraseña debe contener al menos una letra mayúscula.
    -   La contraseña debe contener al menos un símbolo especial.
4. Determinar el conjunto total de contraseñas posibles:
    -   Mediante permutaciones si no se permite repetición.
    -   Mediante potencias si se permite repetición.
5. Aplicar el principio de inclusión-exclusión cuando existan restricciones sobre dígitos, mayúsculas o símbolos.
	-   Calcular el número total de contraseñas válidas.
	-   Mostrar el resultado al usuario.
6. Si ocurre una entrada inválida, mostrar un mensaje de error.

### Pruebas
#### Prueba 1

**Entrada**

Tamaño del alfabeto: 26

Longitud: 4

¿Se permite repetición?: S

¿Debe contener dígito?: N

¿Debe contener mayúscula?: N

¿Debe contener símbolo?: N

**Resultado esperado**

$$
95^4
$$

**Resultado obtenido**

$$ 81450625 $$

#### Prueba 2

**Entrada**

Tamaño del alfabeto: 26

Longitud: 4

¿Se permite repetición?: S

¿Debe contener dígito?: S

¿Debe contener mayúscula?: N

¿Debe contener símbolo?: N

**Resultado esperado**

$$
95^4-85^4
$$

**Resultado obtenido**

$$ 29250000 $$

#### Prueba 3

**Entrada**

Tamaño del alfabeto: 26

Longitud: 6

¿Se permite repetición?: S

¿Debe contener dígito?: S

¿Debe contener mayúscula?: S

¿Debe contener símbolo?: S

**Resultado esperado**

$$ 95^6−85^6−69^6−62^6+59^6+52^6+36^6−26^6 $$

**Resultado obtenido**

$$ 257042986200 $$


### Eficiencia del algoritmo
La complejidad del algoritmo es $O(n)$, donde $n$ corresponde al número utilizado para calcular los factoriales dentro de las permutaciones y la profundidad de la recursión.
