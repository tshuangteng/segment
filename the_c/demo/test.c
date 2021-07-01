#include <stdio.h>

int main()
{
    int a[]={1,2,3};
    char b[]={'a','b','c'};

    printf("%d\n", a);
    printf("%d\n", &a);

    printf("%c\n", b);
    printf("%d\n", &b);

}