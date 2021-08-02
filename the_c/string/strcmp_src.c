/* Copyright (C) 1991-2019 Free Software Foundation, Inc.
   This file is part of the GNU C Library.
   The GNU C Library is free software; you can redistribute it and/or
   modify it under the terms of the GNU Lesser General Public
   License as published by the Free Software Foundation; either
   version 2.1 of the License, or (at your option) any later version.
   The GNU C Library is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
   Lesser General Public License for more details.
   You should have received a copy of the GNU Lesser General Public
   License along with the GNU C Library; if not, see
   <http://www.gnu.org/licenses/>.  */
#include <string.h>
#undef strcmp
#ifndef STRCMP
# define STRCMP strcmp
#endif
/* Compare S1 and S2, returning less than, equal to or
   greater than zero if S1 is lexicographically less than,
   equal to or greater than S2.  */

// c/c++中, 输出字符指针(指针指向的内容是字符)就是输出字符串,程序会自动在遇到'\0'后停止.

int
STRCMP (const char *p1, const char *p2)  // (const char) *p1 表示: 读取p1指向的类型的值,接着转换为const char. 如果p1是double*,则将读取double所有字节的内容,接着转换为const char. [*p1也表示完整的将实参传了进来]
{
    const unsigned char *s1 = (const unsigned char *) p1;  // 初始化一个常量无符号字符指针s1, 为了字符方便比较, 全都转换为无符号常量char指针.
    const unsigned char *s2 = (const unsigned char *) p2;  // (const unsigned char *) p2 表示: 首先指针指向为p2, 然后读取p2中指向位置的第一个字节内容. 即使是double*也只读取第一个字节.
    unsigned char c1, c2;
    do
    {
        c1 = (unsigned char) *s1++;  // 指针后移一位sizeof(char),也就是1字节到后一个字符处.
        c2 = (unsigned char) *s2++;
        if (c1 == '\0')  // 结束循环: 字符指针移动到s1字符串的结尾处'\0', 如果此时的c2还有字符时,相减为负; 如果此时的c2恰好也是'\0',相减为0.
            return c1 - c2;
    }
    while (c1 == c2);  // 循环条件: 通过字符指针s1和s2的自增自减,移动到的字符都是一样的.
    return c1 - c2;  // 结束循环: 字符指针移动到s2字符串的结尾处'\0', 而此时的c1还有字符,相减为正.
}
libc_hidden_builtin_def (strcmp)