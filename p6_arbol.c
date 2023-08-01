#include <stdio.h>
#include <stdlib.h>

//Create a program to graph a christmas tree with the height given by the user

int main()
{
    int height;
    printf("Enter the height of the tree: ");
    scanf("%d", &height);
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < height - i; j++)
        {
            printf(" ");
        }
        for (int k = 0; k < 2 * i + 1; k++)
        {
            printf("*");
        }
        printf("\n");
    }
    for (int i = 0; i < height - 1; i++)
    {
        printf(" ");
    }
    printf("*\n");
    return 0;
}