## Problema 9: Coeficientes Multinomiales
El problema consiste en calcular un coeficiente multinomial. Este coeficiente representa el número de formas en que se pueden distribuir u ordenar $n$ elementos cuando existen grupos de elementos indistinguibles de tamaños $n_1,n_2,n_3,\cdots,n_r$.

#### Formula Utilizada
$$
\binom{n}{n_1,n_2,n_3 , \cdots ,n_r} = \frac{n!}{n_1!n_2!n_3!  \cdots n_r!}
$$

### Algoritmo 
1. Leer la opción seleccionada por el usuario.
2.  Si se ingresa una palabra:
    -   Convertir la palabra a minúsculas.
    -   Contar cuántas veces aparece cada letra distinta.
    -   Acumular el número total de letras $n$.
    -   Multiplicar los factoriales de las repeticiones para construir el denominador.
3.  Si se ingresa una lista de cantidades:
    -   Leer las cantidades separadas por comas.
    -   Sumar todas las cantidades para obtener $n$.
    -   Multiplicar los factoriales de cada cantidad para construir el denominador.
4.  Calcular el factorial de $n$.
5.  Aplicar la fórmula multinomial
6.  Mostrar el resultado obtenido.
7. Si ocurre una entrada inválida, mostrar un mensaje de error.

### Eficiencia del algoritmo
El algoritmo calcula factoriales hasta $n$, por lo que su complejidad temporal es $O(n)$. El uso de memoria es $O(1)$, ya que solo almacena unas pocas variables auxiliares.


