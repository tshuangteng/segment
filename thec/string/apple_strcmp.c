#include <stdio.h>
#import <string.h>


// https://opensource.apple.com/source/Libc/Libc-262/ppc/gen/strcmp.c

/* This routine should be optimized. */

/* ANSI sez:
 *   The `strcmp' function compares the string pointed to by `s1' to the
 *   string pointed to by `s2'.
 *   The `strcmp' function returns an integer greater than, equal to, or less
 *   than zero, according as the string pointed to by `s1' is greater than,
 *   equal to, or less than the string pointed to by `s2'.  [4.11.4.2]
 */

int
strcmp(const char *s1, const char *s2) {
    for (; *s1 == *s2; s1++, s2++)
        if (*s1 == '\0')
            return 0;
    return ((*(unsigned char *) s1 < *(unsigned char *) s2) ? -1 : +1);
}

int main(){
    char str1[] = "hello world";
    char str2[] = "hello worl";

    const char *s1 = str1;
    const char *s2 = str2;

    for ( ; *s1 == *s2; s1++, s2++) {
        if ( *s1 == '\0')
            return 0;
    }
    int res =  ((*(unsigned char *) s1 < *(unsigned char *) s2) ? -1: +1 );
    printf("res, %d\n\n", res);
}