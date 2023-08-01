# Modularización

## Qué es la Modularización

La modularización es una técnica de programación que consiste en dividir un programa en partes más pequeñas, llamadas módulos, que se encargan de realizar una tarea específica. Los módulos se pueden reutilizar en otros programas, lo que permite ahorrar tiempo y esfuerzo al programador. La manera mas sencilla en la que los programadores se familiarizan con la modularización es a través del concepto de la función.

## Funciones

Las funciones son bloques de código que realizan una tarea específica. Las funciones pueden recibir datos de entrada, realizar una serie de operaciones y devolver un resultado. Las funciones son una de las herramientas más poderosas de la programación, ya que permiten reutilizar código y simplificar el desarrollo de programas complejos.

### Declaración de funciones

Las funciones se declaran de manera diferente dependiendo del lenguaje en que estamos trabajando pero todas cuentan con ciertas nociones compartidas entre lenguajes. En el siguiente ejemplo se muestra la declaración de una función en C:

```c
tipo_de_dato nombre_de_funcion(parametros) {
    // Código de la función
}
```

Como se puede ver aquí la función se declara con el tipo de dato que va a devolver, el nombre de la función y los parámetros que recibe. Los parámetros son variables que se declaran dentro de la función y que se utilizan para recibir datos de entrada. En el siguiente ejemplo se muestra la declaración de una función que recibe dos números y devuelve la suma de ambos:

```c
float suma(float a, float b){
return a + b;
}
```

### Llamada a funciones

La declaración de una función no es suficiente para que esta se ejecute, es necesario llamar a la función para que se ejecute el código que contiene. En el siguiente ejemplo se muestra la llamada a la función `suma` que se declaró anteriormente:

```c
int main(){
    float a, b;
    printf("Ingrese el primer número: ");
    scanf("%f", &a);
    printf("Ingrese el segundo número: ");
    scanf("%f", &b);
    printf("La suma de los números es: %f", suma(a, b));
    return 0;
}
```

### Parámetros por defecto(Solo Python)

En ocasiones es necesario que una función tenga un valor por defecto para un parámetro, esto se puede lograr utilizando el operador de asignación `=`. En el siguiente ejemplo se muestra la declaración de una función que recibe un número y devuelve el doble de este, si no se recibe ningún número se devuelve el número 2:

```python
def doble(numero=2):
    return numero * 2
```

Esto es muy útil cuando se tiene una función que recibe muchos parámetros y no se desea tener que especificar todos los parámetros cada vez que se llama a la función.

En C no es posible declarar parámetros por defecto.

### Parámetros variables (Solo Python)

Las funciones pueden recibir un número variable de parámetros, esto se puede lograr utilizando el operador `*` antes del nombre del parámetro. En el siguiente ejemplo se muestra la declaración de una función que recibe un número variable de números y devuelve la suma de todos ellos:

```python
def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado
```

Esto se debe a que el operador `*` permite que el parámetro `numeros` sea una tupla que contiene todos los parámetros que se le pasaron a la función.

En C no es posible declarar parámetros variables, pero se puede simular utilizando la función `va_start` que permite acceder a los parámetros de una función:

```c
float suma(int cantidad, ...){
    float resultado = 0;
    va_list numeros;
    va_start(numeros, cantidad);
    for(int i = 0; i < cantidad; i++){
        resultado += va_arg(numeros, float);
    }
    va_end(numeros);
    return resultado;
}
```

### Funciones anónimas(Solo Python)

Las funciones anónimas son funciones que no tienen nombre, esto se puede lograr utilizando la palabra reservada `lambda` en python:

```python
suma = lambda a, b: a + b
```

En C no es posible declarar funciones anónimas.

### Funciones recursivas

Una función recursiva es una función que se llama a sí misma, esto se puede lograr utilizando la palabra reservada `return` en cualquier función recordando que esa palabra devuelve el valor que se le pasa como parámetro. En el siguiente ejemplo se muestra la declaración de una función que calcula el factorial de un número:

```c
int factorial(int n){
    if(n == 0){
        return 1;
    }
    return n * factorial(n - 1);
}
```

# Construcción de un modulo

## Módulos en C

Un modulo es un archivo que contiene código que se puede importar y utilizar en otros programas. En python los módulos se crean utilizando archivos con extensión `.py` y en C utilizando archivos con extensión `.c` y `.h`.

En C los archivos `.c` contienen el código fuente del módulo y los archivos `.h` contienen la declaración de las funciones que se encuentran en el archivo `.c`. Los headers son necesarios para que el compilador pueda compilar el código fuente del módulo ya que le indican al compilador un prototipo de las funciones que se encuentran en el archivo `.c`, ya entonces el compilador puede compilar el código fuente del módulo sin tener que compilar el código fuente del programa que lo importa.

En el siguiente ejemplo se muestra la creación de un módulo en C:

```c
//Archivo modulo.h

float suma(float a, float b);
```

Como se ve el archivo `.h` contiene la declaración de la función `suma` que se encuentra en el archivo `.c`, no es necesario especificar el código de la función en el archivo `.h` ya que este solo contiene la declaración de la función.

Ya entonces el archivo `.c` contiene el código de la función `suma`:

```c
float suma(float a, float b){
    return a + b;
}
```

El archivo `.c` contiene el código de la función `suma` y el archivo `.h` contiene la declaración de la función `suma`, por lo que el compilador puede compilar el código fuente del módulo sin tener que compilar el código fuente del programa que lo importa.

Entonces siempre y cuando el archivo `.h` contenga la declaración de todas las funciones que se encuentran en el archivo `.c` el compilador puede compilar el código fuente del módulo sin tener que compilar el código fuente del programa que lo importa.

Siempre y cuando nuestro compilador tenga acceso a estos archivos, es decir, que se encuentren en la misma carpeta que el archivo `.c` que los importa, entonces podemos importar el módulo utilizando la palabra reservada `#include`:

```c
#include "modulo.h"
```

Si estos archivos se encuentran en otra carpeta entonces debemos especificar la ruta de la carpeta que contiene estos archivos.

Ya entonces podemos utilizar las funciones que se encuentran en el módulo:

```c
#include "D:\Documentos\modulo.h"

int main(){
    float a, b;
    printf("Ingrese el primer número: ");
    scanf("%f", &a);
    printf("Ingrese el segundo número: ");
    scanf("%f", &b);
    printf("La suma de los números es: %f", suma(a, b));
    return 0;
}
```

**Nota:** En el ejemplo anterior se utilizó la ruta absoluta de la carpeta que contiene los archivos del módulo, pero también se puede utilizar la ruta relativa de la carpeta que contiene los archivos del módulo.

**Nota 2:** En caso de no querer especificar la ruta en cada programa que importe el módulo, se puede especificar la ruta en las variables de entorno del sistema. Para esto se debe ir a `Panel de control > Sistema y seguridad > Sistema > Configuración avanzada del sistema > Variables de entorno` y en la variable `Path` agregar la ruta de la carpeta que contiene los archivos del módulo(esto en Windows).

## Modulos en python
En `python` los módulos se crean utilizando archivos con extensión `.py` y se importan utilizando la palabra reservada `import`:

```python
#Modulo.py
def suma(a, b):
    return a + b
```

Para poder utilizar las funciones que se encuentran en el módulo debemos importarlo utilizando la palabra reservada `import` y especificar el nombre del módulo:

```python
import .modulo as modulo
```

Noten que para importar archivos es necesario añadir el punto `.` antes del nombre del módulo, esto se debe a que el archivo que importa el módulo se encuentra en la misma carpeta que el módulo.

En caso de que el archivo que queremos utilizar como modulo se planee utilizar en otros programas, es posible convertirlo en un paquete de distribución, para esto se debe crear una carpeta que contenga el archivo `.py` y un archivo llamado `__init__.py`.

Este archivo `__init__.py` contará con las instrucciones necesarias para que el módulo se pueda importar en otros programas, todas aquellas que son necesarias al momento en que nuestro código se importa en otro programa. Un ejemplo de esto es la declaración de variables globales.

```python
#__init__.py
import .modulo as modulo

global a
```

Luego entonces es necesaria la creación de un archivo llamado `setup.py` que contendrá las instrucciones necesarias para que el módulo se pueda instalar en el sistema.

```python
#setup.py

import setuptools

setuptools.setup(
    name="modulo",
    version="0.0.1",
    author="Autor",
    author_email="", #Opcional
    python_requires='>=3.6',#Opcional en este caso especifica que el módulo requiere python 3.6 o superior
    requires=['numpy'],#Opcional en este caso especifica que el módulo requiere numpy
    license="MIT",#Opcional en este caso especifica que el módulo tiene licencia MIT
)
```

Este archivo cuenta con la serie de instrucciones necesarias para que el módulo se pueda instalar en el sistema.

Una vez que se ha creado el archivo `setup.py` se puede crear el paquete de distribución utilizando el siguiente comando:

```bash
python setup.py bdist_wheel
```

Este comando crea una carpeta llamada `dist` que contiene el paquete de distribución del módulo en un archivo con extensión `.whl`. Este es un archivo comprimido que contiene el módulo y el archivo `__init__.py` así como todos los archivos necesarios para que el módulo se pueda instalar en el sistema.

Para instalar el módulo en el sistema se debe utilizar el siguiente comando:

```bash
pip install ruta_del_paquete_de_distribucion
```

una vez que el módulo se ha instalado en el sistema se puede importar utilizando la palabra reservada `import`:

```python
import modulo
```
