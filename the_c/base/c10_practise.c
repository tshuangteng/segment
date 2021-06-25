#include <stdio.h>
#include <string.h>

#define StudentNumbers 50
#define NameLength 50

typedef struct {
    int id;
    char name[NameLength];
    int age;
    int score;
    int flag;
} Student;

/*
 // 同上 结构体的定义方法之一
struct Student {
    int id;
    char name[NameLength];
    int age;
    int score;
    int flag;
};

 // 定义结构体 数组
struct Student student;
struct Student students[StudentNumbers];
*/

int add(Student student, Student students[]);
int del(int id, Student students[]);
int display(Student students[]);
int update(int id, Student students[]);
int search(char name[], Student students[]);

int main(){
    int id = -1;
    char name[NameLength];
    int choice = 0;
    int stop = 0;
    Student students[StudentNumbers];
    Student student;

    // 初始化数组: 通过循环
    for(int i=0; i < StudentNumbers; i ++){
        students[i].id = i;
        students[i].flag = 0;
    }

    while (stop==0) {
        printf("-------------------------\n");
        printf("*      学生管理系统      *\n");
        printf("-------------------------\n");
        printf("1 添加\n");
        printf("2 修改成绩\n");
        printf("3 查询\n");
        printf("4 删除\n");
        printf("5 显示学生列表\n");
        printf("0 退出程序\n");
        printf("请直接输入数字选项：");

        scanf("%d\n", &choice);
        switch (choice) {
            case 1:
                printf("请输入学生姓名：");
                scanf("%s", student.name);
                printf("请输入学生的年龄：");
                scanf("%d", &student.age);
                printf("请输入学生成绩：");
                scanf("%d", &student.score);
                add(student, students);
                break;
            case 2:
                printf("请输入要修改成绩的学生编号:");
                scanf("%d", &id);
                update(id, students);
                break;
            case 3:
                printf("请输入要查找的学生姓名:");
                scanf("%s", name);
                search(name, students);
                break;
            case 4:
                printf("请输入要删除的学生编号:");
                scanf("%d", &id);
                del(id, students);
                break;
            case 5:
                display(students);
                break;
            case 0:
                stop = 1;
                break;

            default:
                printf("输入选项有误\n");
                break;
        }
    };

    return 0;
}

int add(Student student, Student students[]) {
    for (int i = 0; i < StudentNumbers; i++){
        if (students[i].flag == 0) {
            strcpy(students[i].name, student.name);  // strcpy用于字符的拷贝
            students[i].age = student.age;
            students[i].score = student.score;
            students[i].flag = 1;
            return 0;
        }
    }
    return 1;
}


int del(int id, Student students[])
{
    for (int i=0; i<StudentNumbers; i++)
    {
        if (students[i].id == id)
        {
            students[i].flag = 0;
            return 0;
        }
    }
    return 1;
}


int display(Student students[])
{
    printf("**************************************\n");
    printf("学生信息列表\n");
    printf("**************************************\n");
    for (int i = 0; i<StudentNumbers; i++)
    {
        if (students[i].flag == 1)
        {
            printf("学生编号: %d, 学生姓名: %s, 年龄: %d, 分数: %d\n", students[i].id, students[i].name, students[i].age, students[i].score);
            return 0;
        }
    }
    printf("没有相关信息可以展示.")
    return 1;
}

int update(int id, Student students[])
{
    int score = -1;
    printf("请输入新的成绩: ");
    scanf("%d", &score);

    for (int i = 0; i< StudentNumbers; i++)
    {
        if (students[i].id == id)
        {
            students[i].score = score;
            return 0;
        }
    }
    return 1;
}


int search(char name[], Student students[])
{
    for (int i = 0;i<StudentNumbers; i++)
    {
        if (strcmp(name, students[i].name)==0) // strcmp 用于字符的大小比较, 不能使用==
        {
            printf("学生编号: %d, 学生姓名: %s, 年龄: %d, 分数: %d\n", students[i].id, students[i].name, students[i].age, students[i].score);
            return 0;
        }
    }
    printf("没有查询到相关信息.");
    return 1;
}


