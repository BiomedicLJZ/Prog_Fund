#include <stdio.h>

int suma(int a, int b)
{
    return a + b;
}
int resta(int a, int b)
{
    return a - b;
}
int multiplicacion(int a, int b)
{
    return a * b;
}
float division(int a, int b)
{
    return (float)a / b;
}
int main()
{
    int a, b;
    printf("Introduce dos numeros: ");
    scanf("%d %d", &a, &b);
    printf("Suma: %d\n", suma(a, b));
    printf("Resta: %d\n", resta(a, b));
    printf("Multiplicacion: %d\n", multiplicacion(a, b));
    printf("Division: %.2f\n", division(a, b));
    return 0;
}
