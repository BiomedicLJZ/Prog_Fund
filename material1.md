# Material 1

## Declaracion de variables

Una variable es un espacio de memoria que almacena un valor. En C se declaran de la siguiente forma:

```c
tipo nombre;
```
Recordando que los tipos de datos son:

* int
* float
* char
* bool

## Asignacion de variables

Asignar un valor a una variable se hace de la siguiente forma:

```c
nombre = valor;
```

## Declaracion e inicializacion de variables

Se puede declarar e inicializar una variable en una sola linea de codigo:

```c
tipo nombre = valor;
```

Con las variables es posible realizar las operaciones matematicas basicas:

* Suma
* Resta
* Multiplicación 
* División

Para realizar estas operaciones se utilizan los operadores:

* +
* -
* *
* /

## Ejemplo

```c
int a = 5;
int b = 2;
int c = a + b;
```

## Funciones

Una función es un conjunto de instrucciones que realizan una tarea especifica. En C se declaran de la siguiente forma:

```c
tipo nombre(tipo parametro1, tipo parametro2, ...){
    // codigo
}
```

Los parametros son variables que se utilizan dentro de la funcion. La funcion puede o no retornar un valor. Para retornar un valor se utiliza la palabra reservada return:

```c
return valor;
```

En el siguiente ejemplo se muestra una funcion que recibe dos parametros y retorna la suma de estos:

```c
int suma(int a, int b){
    return a + b;
}
```

__*Recuerden que las funciones deben ser declaradas antes de ser utilizadas.*__

Entonces un programa con una funcion se veria de la siguiente forma:

```c
int suma(int a, int b){
    return a + b;
}
int main(){
    int resultado = suma(5, 2);
}
```

## Entrada y salida de datos

Un programa que no es capaz de interactuar con el usuario no tiene mucho sentido. Para esto se utilizan las funciones de entrada y salida de datos.

### STDIO.h

Para poder hacer uso de las funciones de entrada y salida de datos se debe incluir la libreria stdio.h:

```c
#include <stdio.h>
```

Una vez añadida esta linea de código al inicio del programa se puede utilizar las funciones de entrada y salida de datos. 

<mark>*Recuerden que las librerias siempre son lo primero que debe estar en el código*<mark>

### Entrada de datos

La entrada de datos se refiere a la lectura de datos desde el teclado. En C se utiliza la funcion scanf:

```c
scanf("%tipo", &variable);
```
Es posible leer varios valores en una sola linea de codigo:

```c
scanf("%tipo1 %tipo2", &variable1, &variable2);
```

### Salida de datos

La salida de datos se refiere a la impresion de datos en la pantalla. En C se utiliza la funcion printf:

```c
printf("texto");
```
Es posible imprimir variables en el texto:

```c
printf("%tipo", variable);
```
_Recuerden que el tipo de la variable debe coincidir con el tipo especificado en el texto._

Para esto utilizamos el caracter `%` seguido del tipo de la variable. 
* %d para enteros
* %i para enteros
* %f para flotantes
* %c para caracteres
* %s para cadenas de caracteres

Es posible imprimir varias variables en una sola linea de codigo:

```c
printf("%tipo1 %tipo2", variable1, variable2);
```

## Ejemplo

```c
int main(){
    int a,b;
    scanf("%d %d", &a, &b);
    printf("%d + %d = %d", a, b, a + b);
}
```

Este programa lee dos numeros enteros desde el teclado y los imprime junto con su suma.

```
"1 + 2 = 3"
```

