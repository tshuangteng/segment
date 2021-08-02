#include <stdio.h>
#include <string.h>
// https://stackoverflow.com/questions/20106732/c-difference-between-unsigned-char-s1-and-unsigned-chars1

int main() {

    char str1[] = "hello world";
    char str2[] = "hello world";
    printf("%s\n",str1);
    printf("%s\n\n",str2);

    const char *p1 = str1;
    const char *p2 = str2;
    printf("%s\n", p1);
    printf("%s\n\n", p2);

    const unsigned char *s1 = (const unsigned char *) p1;
    const unsigned char *s2 = (const unsigned char *) p2;

    printf("%s\n", s1);
    printf("%s\n\n", s2);

//    char test1[] = "hello world";
//    char test2[] = "hello world";
//    int res = strcmp(test1,test2);
//    printf("%d\n\n", res);
//
//    int positive = 'd' - '\0';
//    int negative = '\0' - 'd';
//    printf("%d\n", positive);
//    printf("%d\n", negative);

    return 0;
}