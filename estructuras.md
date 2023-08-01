# Estructuras de control

Las estructuras de control son rutinas que nos permiten controlar el flujo de ejecución de nuestros programas, es decir, nos permiten decidir qué instrucciones se ejecutan y cuáles no. Existen tres tipos de estructuras de control: secuenciales, condicionales y repetitivas.

## Estructuras secuenciales

Las estructuras secuenciales son las más simples, ya que simplemente ejecutan las instrucciones una detrás de otra, en el orden en que aparecen en el código. Por ejemplo, el siguiente código muestra una estructura secuencial:

```c
int a = 5;
int b = 10;
int c = a + b;
```

## Estructuras condicionales

Las estructuras condicionales son aquellas que nos permiten ejecutar una instrucción o un conjunto de instrucciones dependiendo de una condición. Por ejemplo, el siguiente código muestra una estructura condicional:

```c
int a = 5;
int b = 10;
if (a > b) {
    printf("a es mayor que b");
}
```

La estrucura condicional por excelencia es la sentencia `if`, que nos permite ejecutar un conjunto de instrucciones si se cumple una condición. La sintaxis de la sentencia `if` es la siguiente:
    
```c
    if (condición) {
        // instrucciones
    }
```

Para que se ejecuten las instrucciones dentro del bloque de la sentencia `if`, la condición debe ser verdadera. Si la condición es falsa, las instrucciones no se ejecutan. Por ejemplo:

```c
int a = 5;
int b = 10;
if (a > b) {
    printf("a es mayor que b");
}
```

En este caso, la condición `a > b` es falsa, por lo que no se ejecuta el bloque de instrucciones y no se muestra nada por pantalla.

La sentencia `if` también puede tener un bloque `else`, que se ejecuta si la condición es falsa. Por ejemplo:

```c
int a = 5;
int b = 10;
if (a > b) {
    printf("a es mayor que b");
} else {
    printf("a no es mayor que b");
}
```

Para este tipo de estructuras es importante aprender a utilizar los <mark>operadores de comparación</mark>, que nos permiten comparar dos valores y obtener un resultado booleano. Los operadores de comparación son los siguientes:

| Operador | Descripción |
|----------|-------------|
| ==       | Igual       |
| !=       | Distinto    |
| <        | Menor que   |
| >        | Mayor que   |
| <=       | Menor o igual que |
| >=       | Mayor o igual que |

Si quieremos comparar varias condiciones podemos anidar sentencias `if`. Por ejemplo:

```c
int a = 5;
int b = 10;
if (a > 0) {
    if (b > 0) {
        printf("a y b son mayores que 0");
    }
}
```

Esto es bastante tedioso, por lo que podemos utilizar los <mark>operadores lógicos</mark> `&&` (y) y `||` (o), que nos permiten combinar dos o más condiciones. Por ejemplo:

```c
int a = 5;
int b = 10;
if (a > 0 && b > 0) {
    printf("a y b son mayores que 0");
}
```

En este caso, la condición `a > 0 && b > 0` es verdadera, ya que `a` y `b` son mayores que 0. Por lo tanto, se ejecuta el bloque de instrucciones y se muestra el mensaje por pantalla.

### Tablas de verdad

Para comprender los operadores lógicos, es importante entender la tabla de verdad de los operadores lógicos. La tabla de verdad de `&&` es la siguiente:

| A | B | A y B |
|---|---|--------|
| V | V | V      |
| V | F | F      |
| F | V | F      |
| F | F | F      |

La tabla de verdad de `||` es la siguiente:

| A | B | A o B |
|---|---|--------|
| V | V | V      |
| V | F | V      |
| F | V | V      |
| F | F | F      |

### Estrctura selectiva múltiple

La estructura selectiva múltiple es una variante de la estructura condicional, que nos permite ejecutar un conjunto de instrucciones dependiendo de una condición. Por ejemplo, el siguiente código muestra una estructura selectiva múltiple:

```c
int a = 5;
if (a == 0) {
    printf("a es 0");
} else if (a == 1) {
    printf("a es 1");
} else if (a == 2) {
    printf("a es 2");
} else {
    printf("a no es 0, 1 ni 2");
}
```

En este caso, la estructura selectiva múltiple nos permite ejecutar un conjunto de instrucciones dependiendo del valor de `a`. Si `a` es 0, se ejecuta el bloque de instrucciones de la primera condición. Si `a` es 1, se ejecuta el bloque de instrucciones de la segunda condición. Si `a` es 2, se ejecuta el bloque de instrucciones de la tercera condición. Si `a` no es 0, 1 ni 2, se ejecuta el bloque de instrucciones del `else`.

Es importante tener en cuenta que las condiciones se evalúan en orden, por lo que si la primera condición es verdadera, se ejecuta el bloque de instrucciones de la primera condición y no se evalúan las demás condiciones. Por ejemplo, si `a` es 0, se ejecuta el bloque de instrucciones de la primera condición y no se evalúan las demás condiciones.

Ahora, vamos a ver un ejemplo más complejo. El siguiente código muestra una estructura selectiva múltiple:

```c
int a = 5;
if (a == 0) {
    printf("a es 0");
} else if (a == 1) {
    printf("a es 1");
} else if (a == 2) {
    printf("a es 2");
} else if (a == 3) {
    printf("a es 3");
} else if (a == 4) {
    printf("a es 4");
} else if (a == 5) {
    printf("a es 5");
} else if (a == 6) {
    printf("a es 6");
} else if (a == 7) {
    printf("a es 7");
} else if (a == 8) {
    printf("a es 8");
} else if (a == 9) {
    printf("a es 9");
} else {
    printf("a no es 0, 1, 2, 3, 4, 5, 6, 7, 8 ni 9");
}
```

Como podemos ver, este código es bastante tedioso, ya que tenemos que escribir una condición por cada valor posible de `a`. Por suerte, podemos utilizar la estructura `switch` para simplificar este código. La estructura `switch` es una variante de la estructura selectiva múltiple, que nos permite ejecutar un conjunto de instrucciones dependiendo de una condición. Por ejemplo, el siguiente código muestra una estructura `switch`:

```c
int a = 5;
switch (a) {
    case 0:
        printf("a es 0");
        break;
    case 1:
        printf("a es 1");
        break;
    case 2:
        printf("a es 2");
        break;
    case 3:
        printf("a es 3");
        break;
    case 4:
        printf("a es 4");
        break;
    case 5:
        printf("a es 5");
        break;
    case 6:
        printf("a es 6");
        break;
    case 7:
        printf("a es 7");
        break;
    case 8:
        printf("a es 8");
        break;
    case 9:
        printf("a es 9");
        break;
    default:
        printf("a no es 0, 1, 2, 3, 4, 5, 6, 7, 8 ni 9");
        break;
}
```

La estructura `switch` es muy similar a la estructura selectiva múltiple, pero tiene algunas diferencias. En primer lugar, la estructura `switch` no tiene el operador lógico `&&`, por lo que no podemos evaluar varias condiciones. En segundo lugar, la estructura `switch` no tiene el operador lógico `||`, por lo que no podemos evaluar varias condiciones. En cambio podemos evaluar una única condición, que debe ser un entero. Por último, la estructura `switch` no tiene el operador lógico `!`, por lo que no podemos evaluar una condición negada. Pero a pesar de estas limitaciones la estructura `switch` es muy útil, ya que nos permite acceder a una serie de posibles valores de una variable que nosotros determinemos y ejecutar un conjunto de instrucciones dependiendo del valor de la variable.

## Estructuras repetitivas

Las estructuras repetitivas son aquellas que nos permiten ejecutar un conjunto de instrucciones varias veces. Esto es muy útil cuando queremos realizar una tarea repetitiva, como mostrar los números del 1 al 10. Por ejemplo, el siguiente código muestra una estructura repetitiva:

```c
int i = 1;
while (i <= 10) {
    printf("%d\n", i);
    i++;
}
```

Existe una gran variedad de estructuras repetitivas, pero las más importantes son las sentencias `while` y `for`. La sentencia `while` se ejecuta mientras se cumpla una condición. Por ejemplo:

```c
int i = 1;
while (i <= 10) {
    printf("%d\n", i);
    i++;
}
```

En este caso, la sentencia `while` se ejecuta mientras `i` sea menor o igual que 10. En cada iteración, se ejecuta el bloque de instrucciones de la sentencia `while` y se incrementa el valor de `i` en 1. Por lo tanto, la sentencia `while` se ejecuta 10 veces, mostrando los números del 1 al 10.

Existe una variante de la sentencia `while`, que se llama sentencia `do-while`. La sentencia `do-while` se ejecuta mientras se cumpla una condición. Por ejemplo:

```c
int i = 1;
do {
    printf("%d\n", i);
    i++;
} while (i <= 10);
```

La diferencia entre la sentencia `while` y la sentencia `do-while` es que la sentencia `do-while` se ejecuta al menos una vez, mientras que la sentencia `while` no se ejecuta si la condición no se cumple. En este caso, la sentencia `do-while` se ejecuta 10 veces. Es entonces el donde se comprueba si la condición se cumple, y si no se cumple, se sale del bucle.

La sentencia `for` es una variante de la sentencia `while`, que nos permite ejecutar un conjunto de instrucciones varias veces. Por ejemplo:

```c
for (int i = 1; i <= 10; i++) {
    printf("%d\n", i);
}
```

La sentencia `for` se ejecuta mientras se cumpla una condición. En este caso, la sentencia `for` se ejecuta mientras `i` sea menor o igual que 10. En cada iteración, se ejecuta el bloque de instrucciones de la sentencia `for` y se incrementa el valor de `i` en 1. Por lo tanto, la sentencia `for` se ejecuta 10 veces, mostrando los números del 1 al 10.

La estructura de la sentencia `for` es la siguiente:

```c
for (inicialización; condición; incremento) {
    // Bloque de instrucciones
}
```

### Sentencia `break`

La sentencia `break` nos permite salir de un bucle. Por ejemplo:

```c
int i = 1;
while (i <= 10) {
    printf("%d\n", i);
    i++;
    if (i == 5) {
        break;
    }
}
```

La sentencia `break` se ejecuta cuando `i` es igual a 5. En ese momento, se sale del bucle independientemente de si la condición que determina si se ejecuta el bucle se cumple o no.

### Sentencia `continue`

La sentencia `continue` nos permite saltar a la siguiente iteración de un bucle. Por ejemplo:

```c
int i = 1;
while (i <= 10) {
    if (i == 5) {
        i++;
        continue;
    }
    printf("%d\n", i);
    i++;
}
```

La sentencia `continue` se ejecuta cuando `i` es igual a 5. En ese momento, se salta a la siguiente iteración del bucle, es decir, se incrementa el valor de `i` en 1 y se vuelve a comprobar la condición del bucle.

Estas dos sentencias son muy útiles cuando queremos realizar una tarea repetitiva, pero queremos saltar algunas iteraciones del bucle. Son una manera de controlar el flujo de ejecución de un programa.

## Ejericios

### Ejercicio 1

Escribe un programa que lea un número entero y muestre por pantalla si es par o impar.

### Ejercicio 2

Escribe un programa que reciba un numero entero y muestre en pantalla todos los numeros pares desde 0 hasta el numero introducido.

### Ejercicio 3

Escribe un programa que reciba un numero entero y muestre en pantalla `"Fizz"` si el numero es divisible entre 3, `"Buzz"` si es divisible entre 5 y `"FizzBuzz"` si es divisible entre 3 y 5.
