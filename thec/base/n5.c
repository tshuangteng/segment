#include <stdio.h>
#include <string.h>

// 字符串: 字符串数组组成,最后一个元素一定是\0; 初始化直接使用双引号(和数组初始化一样)
int mains() {
    char a[5];  // 只有在初始化时 才能将整个字符串一次性地赋值给它
    char b[] = "abcde";  // 数组的容量一定要比实际存储的字符数量多一, 会在最后隐式地添加一个'\0'
    char c[6] = {'a', 'b', 'c', 'd', 'e', '\0'};  // 逐个字符地给数组赋值并不会自动添加'\0'
    /*
    '\0'是 ASCII 码表中的第 0 个字符，英文称为 NUL. 中文称为“空字符”
    该字符既不能显示，也没有控制功能，输出该字符不会有任何效果
    */
    a[0] = 'H';
    a[1] = 'e';
    a[2] = 'l';
    a[3] = 'l';
    a[4] = '\0';

    printf("a=%s\n", a);

    for (int i = 0; i < 5; i++) {
        printf("a[%d]=%c\n", i, a[i]);
    }

    for (int i = 0; i < 6; i++) {
        printf("b[%d]=%c\n", i, b[i]);
    }

    printf("c=%s\n", c);
    char x[3];
    x[0] = 'H';
    x[1] = 'T';
    x[2] = '!';
    printf("%s\n", x);  // HT!abcde

    char str[] = {'a', 'b', 'c'};
    printf("%s\n", str);  // abcHT!abcde

    char xyz[20] = "";
    printf("%s\n", xyz);

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    printf("---------------\n\n");

    // strlen(str1)     获取str1字符串的长度
    char m[] = "the north face and kith";
    char n[] = "supreme";
    long len = strlen(m);  // 字符串的大小是包含空格和符号的。但是不包含字符数组中的最后一个表示字符串结束的 \0 字符
    printf("the length of the string is %ld\n", len);  // 23
    printf("---------------\n\n");

    // strcpy(str1,str2)	将 str2 中的内容复制到 str1 中
    char o[] = "hype brand: ";
    char p[] = "kith and supreme";
    printf("before copy: %s\n", o);
    strcpy(o, p);
    printf("after copy: %s\n", o);
    printf("---------------\n\n");

    // strcat(str1,str2)	将 str2 连接到 str1 的后面
    char j[] = "hype brand: ";
    char k[] = "kith and supreme";
    strcat(j, k);  // 前面的数组大小要足够大
    printf("after concatenate strings: %s\n", j);
    printf("---------------\n\n");

    // strcmp(str1,str2)	比较两个字符串，如果两个字符串一致则返回 0；如果 str1 大于 str2 则返回正数；如果 str1 小于 str2 则返回负数
    printf("Compare m to m : %d\n", strcmp(m, m));
    printf("Compare m to n : %d\n", strcmp(m, n));
    printf("Compare n to m : %d\n", strcmp(n, m));
    printf("---------------\n\n");

    // strchr(str1,shar1)	在 str1 中查找字符 char1 第一次出现的位置，返回该位置的指针
    char s1[] = "kith and supreme";
    char *pchar;
    pchar = strchr(s1, 'e');  // 严格区分单引号是单字符
    printf("character: %s\n", pchar);

    // strstr(str1.str2)    在 str1 中查找字符串 str2 第一次出现的位置，返回该位置的指针
    pchar = strstr(s1, "it");  // 严格区分双引号是字符串
    printf("string: %s\n", pchar);

    return 0;

}


#include <ctype.h>

// 实现一个函数，函数功能是将一串给定的字符串中的大写字符全部转换为小写字符。
int main() {
    char a[100] = "Welcome to our KITH shop! It is a interest place.", temp;
    char *str="this is demo";  // c 指针使用

    printf("before convert: %s\n", a);

    for (int i = 0; i < strlen(a); i++) {
        temp = tolower(a[i]);
        a[i] = temp;
    }

    printf("after convert: %s\n", a);

    return 0;
}