#include <stdio.h>
#include <string.h>
// https://stackoverflow.com/questions/20106732/c-difference-between-unsigned-char-s1-and-unsigned-chars1

int main() {
    char str1[] = "hello worl";
    char str2[] = "hello world";
    const char *p1 = str1;
    const char *p2 = str2;
    const unsigned char *s1 = (const unsigned char *) p1;
    const unsigned char *s2 = (const unsigned char *) p2;
    unsigned char c1, c2;

    do
    {
        c1 = (unsigned char) *s1++;
        c2 = (unsigned char) *s2++;
        printf("%c\n", c1);
        printf("%c\n\n", c2);
        if (c1 == '\0'){
            printf("negative, c1-c2=%d\n\n", c1 - c2);
            break;
        }
    }
    while (c1 == c2);
    printf("positive, c1-c2=%d\n\n", c1 - c2);

    return 0;
}