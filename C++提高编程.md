本阶段主要针对C++的泛型编程和STL技术

# 1.模板
## 1.1 模板的概念

模板就是建立通用的模具，提高复用性

模板的特点：
- 模板不可以直接使用，他只是一个框架
- 模板的通用并不是万能的


## 1.2 函数模板

- C++另一种编程思想成为泛型编程，主要利用的技术就是模板
- C++提供两种模板机制：函数模板和类模板
  
### 1.2.1 函数模板语法

函数模板作用：
建立一个通用函数，其函数返回值类型可以不具体制定，用一个虚拟的类型来代表


语法：
```cpp
template<typename Ttypename>
```

解释：
template -- 声明创建模板
typename -- 表面其后面的符号是一种数据类型，可用class代替
T -- 通用的数据类型，名称可以替换，通常为大写字母

```C++

//函数模板

//两个整形交换函数
void swapInt(int &a,int &b)
{
    int temp = a;
    a = b;
    b = temp;
}

//两个浮点数交换函数
void swapDouble(double &a,double &b)
{
    double temp = a;
    a = b;
    b = temp;
}

//函数模板
template<typename T> //声明一个模板，告诉编译器后面代码中紧跟的T是一个模板参数

void mySwap(T &a,T &b)
{
    T temp = a;
    a = b;
    b = temp;
}

void test01()
{
    int a = 10;
    int b = 20;
    // swapInt(a,b);

    //利用函数模板交换整型数据
    //两种方式使用函数模板
    //1.自动类型推导
    mySwap(a,b);

    //2.显式指定类型
    mySwap<int>(a,b);

    cout<<"a = "<<a<<endl;
    cout<<"b = "<<b<<endl;

    //利用函数模板交换整型数据


    double c = 1.1;
    double d = 2.2;
    swapDouble(c,d);
    cout<<"c = "<<c<<endl;
    cout<<"d = "<<d<<endl;

    

}


int main()
{
    test01();
    return 0;
}

```

### 1.2.2 函数模板注意事项
注意事项：
- 自动类型推导，必须推导出一致的数据类型T，才可以使用
- 模板必须要确定出T的数据类型，才可以使用


```C++

template<typename T> 

void mySwap(T &a,T &b)
{
    T temp = a;
    a = b;
    b = temp;
}

// 1.自动类型推导，必须推导出一致的数据类型T，才可以使用
void test01()
{
    int a = 10;
    int b = 20;
    char c='a';
    mySwap(a,b);
    mySwap(c,b);//错误，推导不出一致的数据类型T
    cout<<"a = "<<a<<endl;
    cout<<"b = "<<b<<endl;
}

// 2.模板必须要确定出T的数据类型，才可以使用
template<typename T> 

void func()
{
    cout<<"func 调用"<<endl;
}

void test02()
{
    //func(); //错误，必须确定出T的数据类型
    func<int>();
}



int main()
{
    test01();
    return 0;
}


```


```C++
#include <iostream>
#include <typeinfo>
using namespace std;

template<typename T>
void func() {
    cout << typeid(T).name() << " func 调用" << endl;
}

int main() {
    func<int>();
    return 0;
}

```


### 1.2.3 函数模板案例
案例描述：
- 利用函数模板封装一个排序函数，可以对任意数据类型的数组进行排序
- 排序规则从大到小，排序算法为选择排序
- 分别利用char类型和int类型测试排序函数

```C++
#include <iostream>
using namespace std;

template<typename T>
void mySwap(T &a,T &b)
{
    T temp=a;
    a=b; 
    b=temp;
}


template<typename T>
void mySort(T arr[],int len)
{
    for (int i=0;i<len;i++)
    {
        int maxIdx=i;
        for (int j=i+1;j<len;j++)
        {
            if (arr[maxIdx]<arr[j])
            {
                maxIdx=j;
            }
        }
        if(maxIdx!=i)
            {
                mySwap(arr[maxIdx],arr[i]);
            }
    }
}


template<typename T>
void printArray(T arr[],int len)
{
    for (int i=0;i<len;i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}


void test01()
{
    char charArr[]="abcadfa";
    int num=sizeof(charArr)/sizeof(char);
    mySort(charArr,num);
    printArray(charArr,num);

    int intArr[]={1,3,2,4,5};
    num=sizeof(intArr)/sizeof(int);
    mySort(intArr,num);
    printArray(intArr,num);

}


int main()
{
    test01();
    return 0;
}

```

### 1.2.4 普通函数与函数模板的区别

普通函数与函数模板的区别：
- 普通函数调用时可以发生自动转换类型（隐式类型转换），函数模板调用时不能发生自动转换类型
- 函数模板调用时，如果利用自动类型推导，不会发生隐式类型转换
- 如果利用显式指定类型，会发生隐式类型转换

```C++
#include <iostream>
using namespace std;

int myAdd(int a,int b)
{
    return a+b;
}

//函数模板
template<typename T>
T myAdd(T a,T b)
{
    return a+b;
}


void  test01()
{
    int a = 10;
    int b = 20;
    char c='c';//'c'的ASCII码为99
    cout<<"a+b = "<<myAdd(a,b)<<endl;
    cout<<"a+c = "<<myAdd(a,c)<<endl;//可以运算

    //自动类型推导
    //cout<<"a+c = "<<myAdd(a,c)<<endl;//错误，推导不出一致的数据类型T

    //显式指定类型
    cout<<"a+c = "<<myAdd<int>(a,c)<<endl;//可以运算
}

int main()
{
    test01();
    return 0;
}

```

### 1.2.5 普通函数和函数模板的调用规则

调用规则如下：
- 如果普通函数和函数模板都可以调用，优先调用普通函数
- 可以通过空模板参数列表来强制调用函数模板
- 函数模板可以重载
- 如果函数模板可以产生更好的匹配结果，优先调用函数模板


```C++
#include<iostream>
using namespace std;

// 如果普通函数和函数模板都可以调用，优先调用普通函数
// 可以通过空模板参数列表来强制调用函数模板
// 函数模板可以重载
// 如果函数模板可以产生更好的匹配结果，优先调用函数模板

void myPrint(int a,int b)
{
    cout<<"调用普通函数"<<endl;
}

template<typename T>
void myPrint(T a,T b)
{
    cout<<"调用函数模板"<<endl;
}

template<typename T>
void myPrint(T a,T b,T c)
{
    cout<<"调用重载函数模板"<<endl;
}


void test01()
{
    int a = 10;
    int b = 20;
    myPrint(a,b);//调用普通函数,如果只有普通函数声明，没有实现，则会报错，

    myPrint<>(a,b);//调用函数模板,空参数列表

    myPrint(a,b,c);

    //如果函数模板可以产生更好的匹配结果，优先调用函数模板
    char c='c';
    char d='d';
    myPrint(c,d);//调用函数模板
}


int main()
{
    test01();
    return 0;
}

```

### 1.2.6 模板的局限性

局限性：
- 模板的通用性并不是万能的
  
```C++
//例如
template<typename T>
void func(T a,T b)
{
    return a=b;
}

// 如果传入的a,b是数组，就无法实现了

template<typename T>
void func(T a,T b)
{
    if(a>b){}
}
//如果是自定义的数据类型，也无法正常运行

//为解决问题，提供模板的重载，可认为这些特定类型提供的具体化模板

```

```C++
#include<iostream>
#include<string>
using namespace std;

class Person
{
public:
    Person(string name,int age)
    {
        this->m_Name=name;
        this->m_Age=age;
    }

    string m_Name;
    int m_Age;
};


//对比两个数据是否相等
template<typename T>
bool myCompare(T &a,T &b)
{
    if (a==b)
    {
        return true;
    }
    else
    {
        return false;
    }
}

//利用具体化Person的版本实现代码，具体化优先调用
template<> 
bool myCompare(Person &a,Person &b)
{
    if (a.m_Name==b.m_Name&&a.m_Age==b.m_Age)
    {
        return true;
    }
    else
    {
        return false;
    }
}

void test01()
{
    int a = 10;
    int b = 20;
    bool ret=myCompare(a,b);
    if (ret)
    {
        cout<<"a和b相等"<<endl;
    }
    else
    {
        cout<<"a和b不相等"<<endl;
    }
}

void test02()
{
    Person p1("Tom",18);
    Person p2("Tom",18);
    bool ret=myCompare(p1,p2);
    if (ret)
    {
        cout<<"p1和p2相等"<<endl;
    }
    else
    {
        cout<<"p1和p2不相等"<<endl;
    }
}


int main()
{
    test01();
    return 0;
}


```

总结：
- 利用具体化的模板，可以解决自定义类型的通用化
- 学习模板并不是为了写模板，而是在STL能够运用系统提供的模板

## 1.3 类模板

### 1.3.1 类模板语法

类模板作用：
- 建立一个通用类，类中的成员数据类型可以不具体制订，用一个虚拟的类型来代表

```C++
//语法
template<typename T>
class MyTemplate
{
    //类体
};
```

template -- 声明创建模板
typename -- 表面其后面的符号是一种数据类型，可用class代替
T -- 通用的数据类型，名称可以替换，通常为大写字母

```C++
#include<iostream>
#include<string>
using namespace std;

template<class NameType,class AgeType>
class Person
{
public:
    Person(NameType name,AgeType age)
    {
        this->m_Name=name;
        this->m_Age=age;
    }

    void showPerson()
    {
        cout<<"姓名："<<this->m_Name<<endl;
        cout<<"年龄："<<this->m_Age<<endl;
    }

    NameType m_Name;
    AgeType m_Age;
};

void test01()
{
    Person<string,int> p1("Tom",18);
    p1.showPerson();
}


int main()
{
    test01();
    return 0;
}

```

### 1.3.2 类模板与函数模板的区别

类模板与函数模板的区别：
1. 类模板没有自动类型推导的使用方式
2. 类模板在模板参数列表中可以有默认参数
   

```C++
#include<iostream>
#include<string>
using namespace std;

template<typename NameType,class AgeType=int>
class Person
{
public:
    Person(NameType name,AgeType age)
    {
        this->m_Name=name;
        this->m_Age=age;
    }

    void showPerson()
    {
        cout<<"姓名："<<this->m_Name<<endl;
        cout<<"年龄："<<this->m_Age<<endl;
    }

    NameType m_Name;
    AgeType m_Age;
};

//1. 类模板没有自动类型推导的使用方式
void test01()
{
    //Person p1("Tom",18); //错误，无法自动推导类型
    Person<string,int> p1("Tom",18); //正确，手动指定类型   
    p1.showPerson();
}

//2. 类模板在模板参数列表中可以有默认参数
void test02()
{
    Person<string> p1("Mike",20);
    p1.showPerson();
}

int main()
{
    test01();
    test02();
    return 0;
}

```

### 1.3.3 类模板中成员函数创建时机

类模板中成员函数和普通类中成员函数创建实际是有区别的：
- 普通类中成员函数一开始就可以创建
- 类模板中成员函数在调用时才会创建


```C++
#include<iostream>
#include<string>
using namespace std;

class Person1
{
public:
    void showPerson1()
    {
        cout<<"Person1 show"<<endl;
    }
};

class Person2
{
public:
    void showPerson2()
    {
        cout<<"Person2 show"<<endl;
    }
};


template<class T>
class MyClass
{
public:
    T obj;

    //类模板中的成员函数，并不是一开始就创建的，而是在模板调用时再生成
    //类模板中的成员函数
    void func1()
    {
        obj.showPerson1();
    }

    void func2()
    {
        obj.showPerson2();
    }

}

void test01()
{

    MyClass<Person1> p1;
    p1.func1();//正确，调用Person1的showPerson1()函数
    p1.func2();//错误,Person1中没有showPerson2()函数

    MyClass<Person2> p2;
    p2.func1();//错误,Person2中没有showPerson1()函数
    p2.func2();//正确，调用Person2的showPerson2()函数

    

}

int main()
{
    test01();
    return 0;
}

```

###  1.3.4 类模板对象做函数参数

学习目标：
- 类模板实例化出的对象，向函数传参的方式

三种传入方式：
1. 指定传入类型 ---直接显示对象的数据类型
2. 参数模板化 ---将对象的参数变为模板进行传递
3. 整个类模板化 ---将这个对象类型模板化进行传递

```C++
#include<iostream>
#include<string>
using namespace std;


template<class T1,class T2>
class Person
{
public:
    Person(T1 name,T2 age)
    {
        this->m_Name=name;
        this->m_Age=age;
    }

    void showPerson()
    {
        cout<<"姓名："<<this->m_Name<<endl;
        cout<<"年龄："<<this->m_Age<<endl;
    }

    T1 m_Name;
    T2 m_Age;   
};

//1. 指定传入类型 ---直接显示对象的数据类型
void printPerson1(Person<string,int> &p)
{
    p.showPerson(); 
}


void test01()
{
    Person<string,int> p1("Tom",18);
}

//2. 参数模板化 ---将对象的参数变为模板进行传递
template<class T1,class T2>
void printPerson2(Person<T1,T2> &p)
{
    p.showPerson();
    cout<<"T1的类型："<<typeid(T1).name()<<endl;
    cout<<"T2的类型："<<typeid(T2).name()<<endl;
}

void test02()
{
    Person<string,int> p1("Tom",18);
    printPerson2(p1);
}

//3. 整个类模板化 ---将这个对象类型模板化进行传递
template<class T>
void printPerson3(T &p)
{
    p.showPerson();
    cout<<"T的类型："<<typeid(T).name()<<endl;
}

void test03()
{
    Person<string,int> p1("Tom",18);
    printPerson3(p1);
}



int main()
{
    test01();
    test02();
    test03();
    return 0;
}

```

### 1.3.类模板与继承

当类模板碰到继承时，需要注意以下几点：
- 当子类继承的是父类是一个类模板时，子类在声明的时候，要指定出父类中T的类型
- 如果不指定，编译器就无法给子类分配内存
- 如果想灵活指出父类中T的类型，子类也许变成类模板


```C++
#include<iostream>
using namespace std;

template<typename T>
class Base
{
public:
    T m;
};

class Son:public Base<int>  
//class Son:public Base 不加<int>错误,无法确定继承到底有多少个空间
{
public:
    int m;
};

void test01()
{
    Son s1;
}

//如果想灵活指定父类中的T类型，子类也需要变类模板
template<class T1,class T2>  
class Son2:public Base<T2>
{
public:
    Son2()
    {
        cout<<"T1的类型："<<typeid(T1).name()<<endl;
        cout<<"T2的类型："<<typeid(T2).name()<<endl;
    }

    T1 m;
};

void test02()
{
    Son2<int,char> s2;
}

int main()
{
    test01();
    test02();
    return 0;
}

```

总结：如果父类是类模板，子类需要指定出父类中T的类型，否则会报错。


### 1.3.6 类模板成员函数类外实现


```C++
#include<iostream>
#include<string>
using namespace std;


template<class T1,class T2>
class Person
{
public:
    Person(T1 name,T2 age);
    // {
    //     this->m_Name=name;
    //     this->m_Age=age;
    // }

    void showPerson();
    // {
    //     cout<<"姓名："<<this->m_Name<<endl;
    //     cout<<"年龄："<<this->m_Age<<endl;
    // }

    T1 m_Name;
    T2 m_Age;
};

//构造函数类外实现
template<class T1,class T2>
Person<T1,T2>::Person(T1 name,T2 age)
{
    this->m_Name=name;
    this->m_Age=age;
}

//showPerson()函数类外实现
template<class T1,class T2>
void Person<T1,T2>::showPerson()
{
    cout<<"姓名："<<this->m_Name<<endl;
    cout<<"年龄："<<this->m_Age<<endl;
}

void test01()
{
    Person<string,int> p1("Tom",18);
    p1.showPerson();
}

int main()
{
    test01();
    return 0;
}
```

###  1.3.7 类模板分文件编写

问题：
- 类模板中成员函数创建时机是在调用阶段，导致分文件编写时连接不到
  
解决方法：
- 1.直接包含.cpp源文件
- 2.将声明和实现写到同一个文件中，并更改后缀名为.hpp，.hpp是约定的名称，并不是强制


```C++
#include<iostream>
using namespace std;

//第一种方法：直接包含.cpp源文件
#include"person.cpp"

//第二种方法：将声明和实现写到同一个文件中，并更改后缀名为.hpp，.hpp是约定的名称，并不是强制
#include"person.hpp"

// template<class T1,class T2>
// class Person
// {
// public:
//     Person(T1 name,T2 age);

//     void showPerson();

//     T1 m_Name;
//     T2 m_Age;
// };

// template<class T1,class T2>
// Person<T1,T2>::Person(T1 name,T2 age)
// {
//     this->m_Name=name;
//     this->m_Age=age;
// }

// template<class T1,class T2>
// void Person<T1,T2>::showPerson()
// {
//     cout<<"姓名："<<this->m_Name<<endl;
//     cout<<"年龄："<<this->m_Age<<endl;
// }

void test01()
{
    Person<string,int> p1("Tom",18);
    p1.showPerson();
}

int main()
{
    test01();
    return 0;
}

```

源文件
person.cpp  
```cpp

#include"person.h"

template<class T1,class T2>
Person<T1,T2>::Person(T1 name,T2 age)
{
    this->m_Name=name;
    this->m_Age=age;
}

template<class T1,class T2>
void Person<T1,T2>::showPerson()
{
    cout<<"姓名："<<this->m_Name<<endl;
    cout<<"年龄："<<this->m_Age<<endl;
}

```



头文件
person.hpp
```h
#pragma once
#include<iostream>
#include<string>
using namespace std;

template<class T1,class T2>
class Person
{
public:
    Person(T1 name,T2 age);

    void showPerson();

    T1 m_Name;
    T2 m_Age;
};

```


//两个合为一个
```hpp
#include"person.h"
#pragma once
#include<iostream>
#include<string>
using namespace std;

template<class T1,class T2>
Person<T1,T2>::Person(T1 name,T2 age)
{
    this->m_Name=name;
    this->m_Age=age;
}

template<class T1,class T2>
void Person<T1,T2>::showPerson()
{
    cout<<"姓名："<<this->m_Name<<endl;
    cout<<"年龄："<<this->m_Age<<endl;
}

template<class T1,class T2>
class Person
{
public:
    Person(T1 name,T2 age);

    void showPerson();

    T1 m_Name;
    T2 m_Age;
};

```

### 1.3.8 类模板与友元

- 全局函数类内实现，直接在类内声明有元即可
- 全局函数类外实现，需要提前让编译器知道全局函数的存在

```C++
#include<iostream>
#include<string>
using namespace std;

//提前声明Person模板
template<class T1, class T2>
class Person;

//全局函数类外实现
template<class T1, class T2>
void printPerson2(Person<T1, T2> p);


template<class T1, class T2>
class Person
{
    //全局函数类内实现
    friend void printPerson1(Person<T1, T2> p)
    {
        cout << "姓名：" << p.m_Name << endl;
        cout << "年龄：" << p.m_Age << endl;
    }

    //全局函数类外实现 普通函数声明
    //加空模板参数列表
    //为了在类外实现全局函数，需要提前让编译器知道全局函数的存在
    friend void printPerson2<>(Person<T1, T2> p);

public:
    Person(T1 name, T2 age);

    void showPerson();
private:
    T1 m_Name;
    T2 m_Age;
};

//全局函数类外实现
template<class T1,class T2>
void printPerson2(Person<T1,T2> p)
{
    cout<<"姓名："<<p.m_Name<<endl;
    cout<<"年龄："<<p.m_Age<<endl;
}

//1.全局函数类内实现
void test01()
{
    Person<string, int> p1("Tom", 18);
    printPerson1(p1);
}

//2.全局函数类外实现
void test02()
{
    Person<string, int> p2("Jerry", 20);
    printPerson2(p2);
}



int main()
{
    test01();
    test02();
    return 0;
}

```



### 1.3.9 类模板案例

案例描述：
案例描述：实现一个通用的数组类，要求如下：

- 可以对内置数据类型以及自定义数据类型的数据进行存储
- 将数组中的数据存储到堆区
- 构造函数中可以传入数组的容量  
- 提供对应的拷贝构造函数以及operator=防止浅拷贝问题
- 提供尾插法和尾删法对数组中的数据进行增加和删除
- 可以通过下标的方式访问数组中的元素
- 可以获取数组中当前元素个数和数组的容量


```h
#pragma once
#include<iostream>
#include<string>
using namespace std;

template<class T>
class MyArray
{
private:
    T* pAddress; //指针指向堆区的数组

    int m_Capacity;

    int m_Size;
public:

    MyArray(int capacity)
    {
        cout<<"MyArray构造函数"<<endl;
        this->m_Capacity=capacity;
        this->m_Size=0;
        this->pAddress=new T[capacity];
    }

    ~MyArray()
    {
        if (this->pAddress!=nullptr)
        {
            cout<<"MyArray析构函数"<<endl;
            delete[] this->pAddress;
            this->pAddress=nullptr;
        }
    }

    //拷贝构造
    MyArray(const MyArray& arr)
    {
        cout<<"MyArray拷贝构造函数"<<endl;
        this->m_Capacity=arr.m_Capacity;
        this->m_Size=arr.m_Size;
        this->pAddress=new T[arr.m_Capacity];
        for (int i=0;i<this->m_Size;i++)
        {
            this->pAddress[i]=arr.pAddress[i];
        }
    }

    //operator=
    MyArray& operator=(const MyArray& arr)
    {
        if (this!=&arr)
        {
            cout<<"MyArray operator="<<endl;
            //先判断堆区是否有数据
            if (this->pAddress!=nullptr)
            {
                delete[] this->pAddress;
                this->pAddress=nullptr;
                this->m_Capacity=0;
                this->m_Size=0;
            }

            //深拷贝
            this->m_Capacity=arr.m_Capacity;
            this->m_Size=arr.m_Size;
            this->pAddress=new T[arr.m_Capacity];
            for (int i=0;i<this->m_Size;i++)
            {
                this->pAddress[i]=arr.pAddress[i];
            }
        }
        return *this;
    }

    //尾插法
    void pushBack(const T &value)
    {
        if (this->m_Size==this->m_Capacity)
        {
            return;
        }
        this->pAddress[this->m_Size]=value;//尾插法，将数据存储到数组的末尾
        this->m_Size++;//数组大小增加1,更新数组大小
    }

    void popBack()
    {
        //让用户访问不到最后一个元素，即为尾删
        if(this->m_Size==0)
        {
            return;
        }
        this->m_Size--;//数组大小减少1,更新数组大小
    }

    //通过下标的方式访问数组中的元素
    //要重载[]运算符号，需要返回引用类型
    T& operator[](int index)
    {
        return this->pAddress[index];
    }

    //返回数组的容量
    int getCapacity()
    {
        return this->m_Capacity;
    }

    //返回数组的大小
    int getSize()
    {
        return this->m_Size;
    }

};

```

```C++
#include"MyArray.h"
#include<iostream>
using namespace std;

void printIntArray(MyArray<int>& arr)
{
    for (int i = 0; i < arr.getSize(); i++)
    {
        cout << arr[i] << endl;
    }
}


void test01()
{
    MyArray<int> arr1(5);
    MyArray<int> arr2(arr1);
    MyArray<int> arr3(100);
    arr3 = arr2;

    for (int i = 0; i < 5; i++)
    {
        arr1.pushBack(i);
    }

    cout << "arr1的打印输出" <<endl;
    printIntArray(arr1);

    cout << "arr1的容量为" << arr1.getCapacity() << endl;

    cout << "arr1的大小为" << arr1.getSize() << endl;

    
    MyArray<int> arr4(arr1);
    cout << "arr4的打印输出" << endl;
    printIntArray(arr4);
    arr4.popBack();
    cout << "arr4的容量为" << arr4.getCapacity() << endl;
    cout << "arr4的大小为" << arr4.getSize() << endl;
    printIntArray(arr4);
}

class Person
{
public:
    Person(){};
    Person(string name,int age)
    {
        this->m_Name=name;
        this->m_Age=age;
    }

    string m_Name;
    int m_Age;
}

void printPersonArray(MyArray<Person>& arr)
{
    for (int i = 0; i < arr.getSize(); i++)
    {
        cout << "姓名:" << arr[i].m_Name << "年龄:" << arr[i].m_Age << endl;
    }
}

void test02()
{
    MyArray<Person> arr5(5);
    Person p1("张三",18);
    Person p2("李四",20);
    Person p3("王五",22);
    Person p4("赵六",24);
    Person p5("王二",26);

    arr5.pushBack(p1);
    arr5.pushBack(p2);
    arr5.pushBack(p3);
    arr5.pushBack(p4);
    arr5.pushBack(p5);  

    cout<<"arr5的打印输出"<<endl;
    printPersonArray(arr5);

    cout<<"arr5的容量为"<<arr5.getCapacity()<<endl;
    cout<<"arr5的大小为"<<arr5.getSize()<<endl;
}

int main()
{
    test01();
    test02();
    return 0;
}

```

# 2.STL初识

## 2.1 STL的诞生

- C++的面向对象和泛型编程思想，目的就是复用性的提升
- 为了建立数据结构和算法的一套标准，就诞生了STL

## 2.2 STL基本概念

- STL（Standard Template Library）标准模板库
- STL从广义上分为：容器(container)、算法(algorithm)、迭代器(iterator)
- 容器和算法之间通过迭代器进行无缝链接
- STL几乎所有的代码都采用了模板类或者模板函数

## 2.3 STL六大组件

STL大体分为六大组件：容器(container)、算法(algorithm)、迭代器(iterator)、配接器(适配器 ,adapter)、仿函数(function object)、空间配置器(allocator)

1. 容器(container)：各种数据结构，如vector、list、map、set等
2. 算法(algorithm)：各种常用算法，如sort、find、count等
3. 迭代器(iterator):扮演容器与算法之间的桥梁，用于遍历容器中的元素，实现对容器元素的访问和操作
4. 配接器(适配器 ,adapter)：一般用来修饰容器或者仿函数或者迭代器接口的东西
5. 仿函数(function object)：行为类似函数，可作为算法的某种策略  
6. 空间配置器(allocator)：负责空间的配置与管理

## 2.4.STL中的容器、算法、迭代器

- 容器
容器就是将运用最广泛一些数据结构实现出来

常用的数据结构：数组、链表、栈、队列、哈希表、树等

这些容器分为序列式容器和关联式容器

序列式容器：强调值的排序，序列式容器中的每个元素均有固定的位置

关联式容器：二叉树结构，各元素之间没有严格的顺序关系，而是根据键值对的键来组织元素

- 算法：问题之解法
有限的步骤，解决逻辑或数学上的问题

算法分为：质变算法和非质变算法

质变算法：是指在运算过程中会更改区间内的元素的内容，例如：拷贝、替换、删除等

非质变算法：是指在运算过程中不会更改区间内的元素的内容，例如：查找、计数、遍历、寻找极值

- 迭代器：容器和算法之间粘合剂

提供一种方法，使之能够依序寻访某个容器所含的各个元素，而又无需暴露该容器的内部表示方式。

每个容器都有自己专属的迭代器

迭代器使用非常类似于指针，初学阶段我们可以先理解迭代器为指针


迭代器种类：
|种类|功能|支持运算|
|--|--|--|
输入迭代器|	对数据的只读访问|	只读，支持++、==、!=
输出迭代器|	对数据的只写访问|	只写，支持++
前向迭代器|	读写操作，并能向前推进迭代器|	读写，支持++、==、!=
双向迭代器|	读写操作，并能向前和向后操作|	读写，支持++、--
随机访问迭代器|	读写操作，可以以跳跃的方式访问任意数据，功能最强的迭代器|	读写，支持++、--、[n]、-n、<、<=、>、>=


常用的容器中的迭代器种类为双向迭代器，和随机访问迭代器

## 2.5 容器算法迭代器初始

### 2.5.1 vector 存放内置数据类型

容器：vector
算法：for_each
迭代器：vector<int>::iterator

```C++
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void printInt(int val)
{
    cout << val << endl;
}


void test01()
{
    vector<int> v;
    v.push_back(10);
    v.push_back(20);
    v.push_back(30);
    v.push_back(40);

    vector<int>::iterator itBegin = v.begin();
    vector<int>::iterator itEnd = v.end();


    //第一种遍历方式
    while (itBegin != itEnd)
    {
        cout << *itBegin << endl;
        itBegin++;
    }

    //第二种遍历方式
    for (vector<int>::iterator it = v.begin(); it != v.end(); it++)
    {
        cout << *it << endl;
    }

    //第三种遍历方式
    for_each(v.begin(), v.end(), printInt);
    
    //第四种遍历方式
    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i] << endl;
    }
}

int main()
{
    test01();
    return 0;
}


```











