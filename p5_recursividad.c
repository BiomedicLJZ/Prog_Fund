#include <stdio.h>

//Calcular con recursividad la sumatoria en decremento de un numero o sus incrementos si es negativo
int sumatoria(int n){
    if(n == 0)
        return 0;
    else if(n > 0)
        return n + sumatoria(n - 1);
    else
        return n + sumatoria(n + 1);
}
int main(){
    int n;
    printf("Introduce un numero: ");
    scanf("%d", &n);
    printf("La sumatoria de %d es %d", n, sumatoria(n));
    return 0;
}
