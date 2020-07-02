#include <stdio.h>

int main(void)
{
    printf("hello, world\n");
    string name = get_string("Qual seu nome?\n");
    printf("Olá, %s\n", name);
}