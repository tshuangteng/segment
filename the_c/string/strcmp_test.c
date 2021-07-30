#include <stdio.h>
// https://stackoverflow.com/questions/20106732/c-difference-between-unsigned-char-s1-and-unsigned-chars1

int demo_cmp(p1, p2)
        const char *p1;
        const char *p2;
{
    printf("%s\n", p1);
    printf("%s\n\n", p2);

    printf("%d\n", p1);
    printf("%d\n\n", p2);

    const unsigned char *s1 = (const unsigned char *) p1;
    const unsigned char *s2 = (const unsigned char *) p2;
//    const unsigned char *s3 = (const unsigned char) *p2;

    printf("%s\n", s1);
    printf("%c\n", *s1++);
    printf("%c\n\n", *s1);

    printf("%s\n", s2);
    printf("%c\n", *s2++);
    printf("%c\n\n", *s2);

    return 0;
}


int main() {

    char p1[] = "hello world";
    char p2[] = "hello world";
    //    int p1[] = {123};
    //    int p2[] = {789};
    printf("%s\n\n",p1);

    printf("%d\n",*p1);
    printf("%x\n",*p1);
    printf("%d\n",*p2);
    printf("%x\n",*p2);

    return 0;
}