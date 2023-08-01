# Funciones

## ¿Qué es una función?

Una función es un bloque de código que se ejecuta cuando es llamado. estos son definidos por el programador y pueden ser llamados en cualquier momento del programa. Las funciones se utilizan para evitar repetir código, y para organizar el código en bloques lógicos que resuelvan una tarea específica y que puedan ser reutilizados.

## ¿Cual es la estructura de una función?

```c
tipo_retorno nombre_funcion(parametros) {
    // Código de la función
}
```

El tipo de retorno es el tipo de dato que devuelve la función, si no devuelve nada se utiliza `void`. Los parámetros son los datos que recibe la función, si no recibe nada se utiliza `void`. El nombre de la función es el nombre que se le asigna a la función, este debe ser único en el programa. El código de la función es el código que se ejecuta cuando se llama a la función. Una función puede tener cero o más parámetros, y puede devolver cero o más valores. 

## ¿Cómo se llama a una función?

```c
nombre_funcion(parametros);
```

Para nosotros utilizar una función debemos llamarla, para esto debemos escribir el nombre de la función y entre paréntesis los parámetros que recibe la función. Si la función no recibe parámetros, se deben escribir los paréntesis vacíos. Esto es lo que se conoce como **invocación** de la función. 

Las funciones deben ser declaradas antes de ser utilizadas, es decir, antes de llamarlas. Por lo que en C las funciones se declaran antes del `main()`.

## ¿Es obligatorio que una función devuelva un valor?

No, una función puede no devolver ningún valor, en este caso se utiliza `void` como tipo de retorno.

## ¿Es obligatorio que una función reciba parámetros?

No, una función puede no recibir ningún parámetro, en ese caso simplemente se escriben los paréntesis vacíos.

## ¿Qué es un parámetro?

Un parámetro es una variable que se utiliza para recibir datos de la función. Los parámetros son variables locales a la función, es decir, no pueden ser utilizadas fuera de la función. Los parámetros se declaran como cualquier otra variable, pero dentro de la función.

```c
void nombre_funcion(int parametro) {
    // Código de la función
}
```

## ¿Qué es un argumento?

Un argumento es el valor que se le pasa a la función cuando se la invoca. Los argumentos son variables locales al programa, es decir, no pueden ser utilizadas fuera del programa. Los argumentos se declaran como cualquier otra variable, pero fuera de la función.

```c
int main() {
    int argumento = 5;
    nombre_funcion(argumento);
}
```

##Ejemplo

```c
#include <stdio.h>

void saludar() {
    printf("Hola mundo!\n");
}
int suma(int a, int b) {
    return a + b;
}
int main() {
    saludar();
    int resultado = suma(5, 3);
    printf("El resultado es: %d\n", resultado);
    return 0;
}
```

## ¿Qué es una función recursiva?

Una función recursiva es una función que se llama a sí misma. Las funciones recursivas son muy útiles para resolver problemas que se pueden dividir en subproblemas similares.

### Ejemplo

```c
#include <stdio.h>

int factorial(int n) {
    if (n == 0) {
        return 1;
    }
    return n * factorial(n - 1);
}
int main() {
    int n = 5;
    int resultado = factorial(n);
    printf("El factorial de %d es %d\n", n, resultado);
    return 0;
}
```

## ¿Qué es una función anónima?

Una función anónima es una función que no tiene nombre. Las funciones anónimas son muy útiles para pasar como parámetro a otras funciones.

### Ejemplo

```c
#include <stdio.h>

void imprimir(int (*funcion)()) {
    printf("El resultado es: %d\n", funcion());
}
int main() {
    imprimir([]() { return 5; });
    return 0;
}
```

## Ejercicios

1. Escribir una función que reciba un número y devuelva su factorial.
2. Escribir una función que reciba un número y devuelva su valor absoluto.
3. Escribir una función que reciba un número y devuelva su cuadrado.
4. Escribir una función que calcule el máximo común divisor de dos números.

## Ejercicios avanzados

1. Escribir una función que reciba un número y devuelva `true` si es primo y `false` si no lo es.
2. Escribir una función que reciba un numero y devuelva `true` si es palindromo y `false` si no lo es.


<mark>**Recuerden que todas sus funciones deben implementarse en un archivo .c y usarse en su main()**<mark>