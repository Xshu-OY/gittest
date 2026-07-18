# 2 引用

## 2.1 引用的基本用法
作用：给变量区别名
语法：数据类型 & 引用名 = 变量名;

## 2.2 应用的注意事项
1.引用必须初始化
2.引用在初始化后，不可以改变

## 2.3 引用做函数参数
作用：函数传参时，可以利用引用的技术实现参数的传递
有点：可以简化指针修改实参
总结：引用传递和地址传递的效果是一致的，语法更简单

## 2.4 引用做函数返回值
作用：引用可以作为函数的返回值存在
注意：不要返回局部变量的引用
用法：函数调用作为左值

e.g
```C++
test()=100;
test()返回一个值的引用，将100复制给这个值
```

## 2.5 引用的本质
本质：引用的本质在c++内部实现是一个指针常量
结论：引用技术更简单，所有的指针操作编译器帮我们做了

## 2.6 常量引用
作用：常量引用主要用来修饰形参，防止误操作
在函数形参列表中，用const修饰形参，防止形参改变实参

---

# 3函数提高

## 3.1 函数默认参数
函数形参列表中的形参数可以有默认值
语法： 返回值类型 函数名 (参数=默认值){}

如果有传入数据，就用自己的数据，如果没有，就用默认值

注意事项：
1.如果某个位置已经有了默认参数，那么从这个位置往后，从左到右都要有默认值

2.函数声明和函数定义中，只能有一个有默认值

## 3.2 函数占位参数
C++中函数的形参列表里可以有占位参数，用来做占位，调用函数是必须填补该位置

语法： 返回值类型 函数名 (数据类型){}

注意点：占位参数还可以有默认值，传的时候可以不传

## 3.3 函数重载-基本语法

作用：函数名可以相同，提高复用性

函数重载满足条件：
1.同一个作用域下
2.函数名相同
3.函数参数类型不同或者个数不同或者顺序不同

注意：函数的返回值不可以作为函数重载的条件,即只有返回值不同，函数重载是不可以的

## 3.4 函数重载-注意事项

1.引用作为函数重载的条件：

e.g
```C++  
void func(int &a){}
void func(const int &a){}

int a=10;
func(a);   ___调用第一个，a数据在栈区，为局部变量___

func(10) __调用第二个，因为引用必须为堆区或者栈区的数据，而10为常量，所以int &a=10 不合法,const int &a=10合法__
```


2.函数重载遇到默认参数

e.g
```C++
void func(int a,int b=10){}
void func(int a){}

func(10);

__当函数重载遇到默认参数，会遇到二义性调用第一个和第二个都行，不知道调用哪个，要避免__

```

---

# 4 类和对象

C++面向对象的三大特性
1.封装
2.继承
3.多态

C++认为对象有其属性和行为

具有想用性质的对象我们可以抽象为一个类


## 4.1 封装

### 4.1.1 封装的意义

封装的意义（一）：
1.将属性和行为作为一个整体，提高代码的复用性
2.可以隐藏内部实现，保护数据的安全性
3.将属性和行为加以权限控制

```C++
****封装的实现****
语法：
class 类名{
    访问权限:
    属性;
    行为;
}; 

```

封装的意义（二）：
类在设计时，可以把属性和行为放在不同的权限下，加以控制
访问权限有三种：
1.public 公共权限  类内和类外都可以访问到
2.private 私有权限  类内可以访问到，类外不可以访问到
3.protected 受保护权限  类内可以访问到，类外不可以访问到，但是可以被继承类访问  


### 4.1.2 struct和class的区别
在C++中，struct和class的区别主要在于访问权限的默认值不同

区别：
struct默认访问权限为public
class默认访问权限为private

### 4.1.3 成员属性设置为私有
优点：
1.将所有的成员属性设置为私有，可以自己控制读写权限
2.对于写权限，我们可以监测数据的有效性


## 4.2 对象的初始化和清理

### 4.2.1 构造函数和析构函数
1.对象的初始化和清理有两个重要的安全问题：
    (1)一个对象或者变量没有初始化，对其使用后果也是未知
    (2)使用完一个变量或对象，没有及时清理，也会造成安全问题

构造函数和析构函数自动完成对象的初始化和清理，如果我们不提供构造和析构函数，编译器会自动为我们提供默认的构造函数和析构函数，默认的构造函数和析构函数是空的，不会做任何操作

构造函数：创建对象时为对象的成员属性赋值
析构函数：对象销毁时，系统自动调用

___构造函数语法___
类名(){}
1.构造函数没有返回值也不用写void
2.函数名称和类名相同
3.构造函数可以有参数，因此可以发生重载
4.程序在调用对象时会自动调用构造函数，无需手动调用，而且只会调用一次

___析构函数语法___
~类名(){}
1.析构函数，没有返回值也不用写void
2.函数名称与类名相同，在名称前加上符号~
3.析构函数不可以有参数，因此不可以发生重载
4.程序在对象销毁前会自动调用析构，无需手动调用，而且只会调用一次


### 4.2.2 构造函数的分类和调用

分类：
按参数分：有参构造和无参构造（默认构造）
按类型分：普通构造和拷贝构造

e.g
```C++
class Person
{
public:
    Person(){}

    Person(int a){}

    Person(const Person &p){}  __拷贝构造__
};
```


调用：
括号法
```C++
Person p;  __默认构造,无参构造函数__
Person p1(1);  __有参构造,有参构造函数__
Person p2(p1);  __拷贝构造,拷贝构造函数__

调用默认构造函数时，不要加()
Person p3() __编译器会认为是一个函数的声明，而不是对象的创建__

显示法
Person p1();
Person p2=Person(10); __有参构造,有参构造函数__
Person p3=Person(p2); __拷贝构造,拷贝构造函数__

Person(10); __匿名对象，特点：当前执行结束后，系统会自动收回掉匿名对象__

不要用拷贝构造函数初始化你名对象，编译器会认为
Person (p3)===Person p3; 对象的声明

影式转化法
Person p4=10;  __有参构造,有参构造函数__
相当于Person p4(10)，Person p4=Person(10);

Person p5=p4;  __拷贝构造,拷贝构造函数__
```


### 4.2.3 拷贝构造函数调用时机

三种情况：
1.使用一个已经创建完毕的对象初始化一个新的对象
2.值传递的方式给函数参数传值，是一个临时的对象
3.以值方式返回局部对象


### 4.2.4 构造函数调用规则
默认情况下，C++编译器至少给一个类添加3个函数
1.默认构造函数（无参，函数体为空）
2.默认析构函数（无参，函数体为空）
3.默认拷贝构造函数，对属性进行值拷贝

构造函数调用规则如下：
1.有自定义的有参构造函数，C++不在提供默认无参构造函数，但会提供默认拷贝构造
2.有自定义的拷贝构造函数，C++不再提供其他普通构造函数


### 4.2.5 深拷贝与浅拷贝

浅拷贝：简单的赋值拷贝操作
问题：
堆区的内存重复释放


深拷贝：在堆区重新申请空间，进行拷贝操作


### 4.2.6 初始化列表
作用：用来初始化属性

语法：构造函数():属性1(值1),属性2(值2)...{}

```C++
class Person{
    public:
        int ma;
        int mb;
    
    Person(int a,int b):ma(a),mb(b)
    {
        cout<<"初始化列表"<<endl;
    }
};
```



### 4.2.6 类对象作为类成员

对象成员：类中的成员是另一个类对象
e.g

```C++
class A{};
class B{
    public:
        A a;
};
```

当其它类对象作为当前类的成员时，构造时先构造类对象，在构造自身，析构的顺序与构造相反 

```C++

class Phone{
    public:
    Phone(string pName){
        cout<<"Phone构造函数"<<endl;
        m_PName=pName;
    }

    ~Phone(){
        cout<<"Phone析构函数"<<endl;
    }

    string m_PName;
};

class Person{
    public:
    Person(string name,string pName):m_Name(name),m_Phone(pName){
        cout<<"Person构造函数"<<endl;
    }

    ~Person(){
        cout<<"Person析构函数"<<endl;
    }

    Phone m_Phone;
    string m_Name;
};

void test()
{
    Person p("张三","max");
}

int main()
{
    test();
    return 0;
}


```

### 4.2.8 静态成员
静态成员就是在成员变量和成员函数前加上static关键字，

静态成员分为：

静态成员变量
1.所有对象共享同一个分数据  
2.在编译阶段分配内存
3.类内声明，类外初始化

e.g
```C++
class Person{
public:
    static int m_A;

private:
    static int m_B;  //静态成员变量也是有访问权限的

};

int Person::m_A=100;
int Person::m_B=200;


void test()
{
    //静态成员变量 不属于某个对象上，所有对象都共享一份数据
    //静态成员变量两种访问方式

    //1.通过对象进行访问
    Person p;
    cout<<p.m_A<<endl;
    
    //2.通过类名进行访问
    cout<<Person::m_A<<endl;


    cout<<Person::m_B<<endl; //错误，私有静态成员变量类外访问不到
}


int main()
{
    test();
    return 0;
}

```



静态成员函数
1.所有对象共享同一个函数
2.静态成员函数只能访问静态成员变量和静态成员函数

```C++
class Person{

public:
    //静态成员函数

    static void func(){
        cout<<"静态成员函数func调用"<<endl;

        m_A=200;
        m_B=300;//错误，静态成员变量只能在静态成员函数中访问,不可以访问非静态成员变量
    }

    static int m_A;
    int m_B;

private:
    static void func2(){
        cout<<"静态成员函数func2调用"<<endl;
    }

};
int Person::m_A=100;

void test()
{
    //静态成员函数两种访问方式
    //1.通过对象进行访问
    Person p;
    p.func();
    
    //2.通过类名进行访问
    Person::func();
    
    Person::func2();//错误，私有静态成员函数类外访问不到
}



int main()
{
    test();
    return 0;
}


```

---


## 4.3 C++对象模型和this指针

### 4.3.1 成员变量和成员函数分开存储

在C++中，类内成员变量和成员函数分开存储
只有非静态成员变量才属于累的对象上

```C++
class Person{
public:
    int mA; //非静态成员变量，属于对象上

    static int m_B;//静态成员变量，不属于类对象上

    void func(){} //非静态成员函数，不属于对象上

    static void func2(){} //静态成员函数，不属于类对象上
};

void test01(){
    Person p;
    //空对象占内存空间为：1
    //C++编译器会给每个空对象也分配一个字节空间，是为了区分空对象占内存的位置
    //每个空对象也应该有一个独一无二的内存地址
    cout<<"size of p="<<sizeof(p)<<endl;
}

int main()
{

    return 0;
}

```


### 4.3.2 this指针概念

在C++中，类内的成员变量和成员函数分开存储
每一个非静态成员函数只会诞生一份函数实例，也就是说多个同类型的对象会共用一块代码

问题：这一块代码怎么区分是哪个对象调用自己的

this指针：指向被调用的成员函数所属的对象

this指针是隐含每一个非静态成员函数内的一种指针
this指针不需要定义，直接使用即可

this指针的用途：
当形参和成员变量同名时，可用this指针来区分
在类的非静态成员函数中返回对象本身，可使用return *this

```C++
class Person
{
public:
    Person(int age)
    {
        age=age;//错误，形参和成员变量同名，不能直接赋值

        //解法
        //2.使用this指针
        this->age=age;

    }

    //int age-->m_Age;  //1.改变成员变量名
    int age;


    //不加&，返回的是一个新的对象，应用返回的一直是p2
    Person& PersonAddAge(Person &p)
    {
        this->age+=p.age;
        return *this;
    }
}



//1.解决名称冲突
void test01()
{
    Person p(18);
    cout<<p.age<<endl;
}

//2.返回对象本身使用*this
void test02()
{
    Person p1(10);
    Person p2(10);
    p2.PersonAddAge(p1).PersonAddAge(p1).PersonAddAge(p1);
    cout<<p2.age<<endl;
}


int main()
{
    test01();
    test02();
    return 0;
}

```

### 4.3.3 空指针访问成员函数

C++中空指针也是可以调用成员函数的，但是也要注意有没有用到this指针

如果用到this指针，需要加以判断保证代码的健壮性

```C++
class Person{
public:
    void ShowClassName(){
        cout<<"this is Person class"<<endl;
    }

    void showPersonAge()
    {
        //报错原因是因为传入的指针是NULL
        cout<<"age="<<mAge<<endl;
    }

    int mAge;
}


void test01()
{
    Person *p=NULL;

    p->ShowClassName();

    p->showPersonAge(); //错误，空指针调用成员函数，会报错
}


int main()
{
    test01();
    return 0;
}

```


### 4.3.4 const修饰成员函数

常函数：
1.成员函数后加const，称这个函数是常函数
2.常函数内部不可以修改成员属性
3.成员属性声明时加关键字mutable，在常函数中依然可以修改

常对象：
1.声明对象加const称该对象为常对象
2.常对象只能调用常函数

```C++
class Person
{
public:

    //this指针的本质 是指针常量   指针的指向是不可以改变的
    //const Person*const this;
    //在成员函数后面加const，修饰的是this的指向，让指针指向的值也不可以修改
    void showPerson() const
    {
        this->m_A=100;  //错误，常函数内部不能修改成员属性
        this =NULL;  //错误，this指针指向不能修改
        this->m_B=100;  //正确，m_B是特殊值，常对象可以修改特殊变量
    }

    int m_A;
    mutable int m_B;  //特殊变量，即使在常函数中，也可以修改这个值，加关键字mutable
}

void test01()
{
    Person p;
    p.showPerson();
}


void test02()
{
    const Person p;//在对象前加const，称该对象为常对象
    //p.m_A=100; //错误，常对象不能修改成员属性
    p.m_B=100; //正确，m_B是特殊值，常对象可以修改特殊变量

    p.showPerson(); //正确，常对象可以调用常函数
    p.func(); ///错误，常对象不能调用普通成员函数，因为普通成员函数可以修改属性
}


int main()
{
    test01();
    test02();
    return 0;
}
```

## 4.4 友元

程序里有些私有属性也想让类外特殊的一些函数或者类进行访问，需要用到友元函数


目的：让一个函数或者类访问另一个类中的私有成员

关键字 friend

有缘的三种实现
1.全局函数做友元
2.类做友元
3.成员函数做友元



1.全局函数做友元
```C++

class Building
{
    //告诉编译器goodguy全局函数是building类的友元函数，可以访问类中的私有内容
    friend void goodguy(Building *building);
public:
    Building()
    {
        m_sitroom="客厅";
        n_bedroom="卧室";
    }

public:
    string m_sitroom;

private:
    string n_bedroom;
}

//全局函数
void goodguy(Building *building)
{
    cout<<"good guy is"<<building->m_sitroom<<endl;

    //cout<<"good guy is"<<building->n_bedroom<<endl; //错误，私有成员不能直接访问

    //加了friend void goodguy(Building *building)就正确了
    cout<<"good guy is"<<building->n_bedroom<<endl;
}


void test01()
{
    Building building;
    goodguy(&building);
}

int main()
{
    test01();
    return 0;
}

```

2.类做友元

```C++
class Building;


class Goodguy
{
public:
    Goodguy();

    void visit();

    Building* building;
};

class Building
{
    //告诉编译器Goodguy类是building类的友元类，可以访问类中的私有内容
    friend class Goodguy;

public:
    Building();

public:
    string m_sitroom;

private:
    string n_bedroom;
}


//类外定义成员函数
Building::Building()
{
    m_sitroom="客厅";
    n_bedroom="卧室";
}

Goodguy ::Goodguy()
{
    //创建一个Building对象
    building=new Building();
}

void Goodguy ::visit()
{
    cout<<"good guy is"<<building->m_sitroom<<endl;
    cout<<"good guy is"<<building->n_bedroom<<endl;
}

void test01()
{
    Goodguy gg;
    gg.visit();
}

int main()
{
    test01();
    return 0;
}

```


3.成员函数做友元

```C++
class Building;

class Goodguy
{
public:
    Goodguy();

    void visit(); //visit可以访问类中的私有成员

    void visit2();  //visit2不可以访问类中的私有成员

    Building* building;
}；

class Building
{
    //告诉编译器visit函数是building类的友元函数，可以访问类中的私有成员
    friend void Goodguy ::visit();

public:
    Building();

public:
    string m_sitroom;

private:
    string n_bedroom;
};

//类外定义成员函数
Building::Building()
{
    m_sitroom="客厅";
    n_bedroom="卧室";
}

Goodguy ::Goodguy()
{
    //创建一个Building对象
    building=new Building();
}



void Goodguy ::visit()
{
    cout<<"visit函数正在访问"<<building->m_sitroom<<endl;
    cout<<"visit函数正在访问"<<building->n_bedroom<<endl;
}



void Goodguy ::visit2()
{
    cout<<"visit2函数正在访问"<<building->n_bedroom<<endl;
    //cout<<"visit2函数正在访问"<<building->m_sitroom<<endl; //错误，私有成员不能直接访问
}

void test01()
{
    Goodguy gg;
    gg.visit();
    gg.visit2();
}


int main()
{
    test01();
    return 0;
}


```

## 4.5 运算符重载

运算符重载：对已有的运算符进行重新定义，赋予其另一种功能，以适应不同的数据类型


### 4.5.1 加号运算符重载

```C++


//加号运算符
int a=10;
int b=20;
int c=a+b;

//加号运算符重载

class Person
{
public:
    int m_A;
    int m_B;

    //1.成员运算符重载加号
    Person operator+(Person &p)
    {
        Person temp;
        temp.m_A=this->m_A+p.m_A;
        temp.m_B=this->m_B+p.m_B;
        return temp;
    }
};

//2.全局函数重载加号
Person operator+(Person &p1,Person &p2)
{
    Person temp;
    temp.m_A=p1.m_A+p2.m_A;
    temp.m_B=p1.m_B+p2.m_B;
    return temp;
}

//3.运算符重载，也可以发生函数重载
Person operator+(Person &p,int n)
{
    Person temp;
    temp.m_A=p.m_A+n;
    temp.m_B=p.m_B+n;
    return temp;
}



void test01()
{
    Person p1;
    p1.m_A=10;
    p1.m_B=20;

    Person p2;
    p2.m_A=30;
    p2.m_B=40;

    //1.成员运算符重载加号
    //本质：p3=p1.operator+(p2);

    //2.全局函数重载加号
    //本质：p3=operator+(p1,p2);

    Person p3=p1+p2;

    //运算符重载，也可以发生函数重载
    Person p4=p1+10; //Person + int

    cout<<"p3.m_A="<<p3.m_A<<endl;
    cout<<"p3.m_B="<<p3.m_B<<endl;

    cout<<"p4.m_A="<<p4.m_A<<endl;
    cout<<"p4.m_B="<<p4.m_B<<endl;
}

int main()
{
    test01();
    return 0;
}


```


### 4.5.2 左移运算符重载

作用：可以输出自定义数据类型

```C++

///左移运算符重载

class Person
{
    //私有化加友元
    friend ostream& operator<<(ostream &cout,Person &p);

public:
Person(int a,int b){
    m_A=a;
    m_B=b;
}

// public:
private:
    int m_A;
    int m_B;

    //1.利用成员函数重载 左移运算符
    //p.operator<<(cout) 简化版本 p<<cout
    //不会利用成员函数重载<<运算符，因为<<运算符是左关联的，先调用左操作数的成员函数,再调用右操作数的成员函数
    //无法实现cout在左侧
    // void operator<<(cout)
    // {
        
    // }
};


// 只能利用全局函数重载左移运算符
ostream& operator<<(ostream &cout,Person &p)
{
    cout<<"p.m_A="<<p.m_A<<" p.m_B="<<p.m_B<<endl;d
}

void test01()
{
    Person p1(10,20);
    
    cout<<"p1.m_A="<<p1.m_A<<endl;
    cout<<"p1.m_B="<<p1.m_B<<endl;


    //cout<<p1; //错误,没有与操作数匹配的“<<”运算符

    // cout<<p<<endl; //错误，返回void，不能链式调用，用ostream&返回值

    cout<<p1<<endl;
}

int main()
{
    test01();
    return 0;
}


```


总结：左移运算符配合友元可以实现输出自定义数据类型


###  4.5.3 递增运算符重载

作用:通过重载递增运算符，实现自己的整形数据


 ```C++
//重载递增运算符



//自定义整形

class MyInteger
{
    //私有化加友元
    friend ostream& operator<<(ostream &cout,MyInteger &myint);

public:
    MyInteger(){
        m_A=0;
    }

    //重载前置++运算符  返回引用是为了一直对一个数据进行递增操作
    MyInteger& operator++()    
    {
        //先进行++运算
        m_Num++;
        //在将自身做返回
        return *this;
    }

    //重载后置++运算符
    //void operator++(int) int代表占位参数，可以用于区分前置++和后置++运算符
    MyInteger operator++(int)
    {
        //先记录当前结果
        MyInteger temp=*this;
        
        //再递增
        m_Num++;
        //返回记录的结果
        return temp;
    }



private:
    int m_Num;
};

//重载<<运算符
ostream& operator<<(ostream &cout,MyInteger &myint)
{
    cout<<myint.m_Num;
    return cout;
}



void test01()
{
    MyInteger myint;
    cout<<++(++myint)<<endl;
    cout<<myint<<endl;
    
}


void test02()
{
    MyInteger myint;
    cout<<myint++<<endl;
    cout<<myint<<endl;
}
 

int main()
{
    test01();
    return 0;
}


 ```

### 4.5.4 赋值运算符重载

C++编译器至少给一个类添加4个函数
1.默认构造函数(无参，函数体为空)
2.默认析构函数(无参，函数体为空)
3.拷贝构造函数,对属性进行只拷贝
4.赋值运算符operator=对属性进行值拷贝

如果类中有属性指向堆区，做赋值操作是也会出现深浅拷贝问题


```C++
//赋值运算符重载

class Person
{
public:
    Person(int age)
    {
        m_Age=new int (age);
    }

    ~Person()
    {
        if (m_Age!=NULL)
        {
            delete m_Age;
            m_Age=NULL;
        }
    }


    //重载赋值运算符
    Person& operator=(Person &p)
    {
        //编译器提供的是浅拷贝
        //m_Age=p.m_Age;

        //应该先判断是是否有属性再堆区，如果有显示放干净，然后再深拷贝
        if (m_Age!=NULL)
        {
            delete m_Age;
            m_Age=NULL;
        }

        //深拷贝
        m_Age=new int (*p.m_Age);

        return *this;
    }

    int *m_Age;
};

void test01()
{
    Person p1(18);

    Person p2(20);
    cout<<"p1年龄="<<*p1.m_Age<<endl;

    cout<<"p2年龄="<<*p2.m_Age<<endl;

    p2=p1; //赋值操作
    cout<<"p2年龄="<<*p2.m_Age<<endl;

    p3=p2=p1; //赋值操作
    cout<<"p3年龄="<<*p3.m_Age<<endl;

}

int main()
{
    int a=10;
    int b=20;
    int c=30;

    c=a=b;

    cout<<"a="<<a<<endl;
    cout<<"b="<<b<<endl;
    cout<<"c="<<c<<endl;

    



    test01();
    return 0;
}
```



### 4.5.5 关系运算符重载

作用:重载关系运算符，可以让两个自定义类型对象进行对比操作

```C++
//关系运算符重载


class Person
{
public:
    Person(string name,int age)
    {
        m_Name=name;
        m_Age=age;
    }

    //重载==运算符
    bool operator==(Person &p)
    {
        if (this->m_Name==p.m_Name&&this->m_Age==p.m_Age)
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    //重载!=运算符
    bool operator!=(Person &p)
    {
        if (this->m_Name==p.m_Name&&this->m_Age==p.m_Age)
        {
            return false;
        }
        else
        {
            return true;
        }
    }

    string m_Name;
    int m_Age;
};



void test01()
{
    Person p1("Tom",18);
    Person p2("Tom",20);

    if (p1=p2)
    {
        cout<<"p1=p2"<<endl;
    }
    else
    {
        cout<<"p1!=p2"<<endl;
    }

    if (p1!=p2)
    {
        cout<<"p1!=p2"<<endl;
    }else{
        cout<<"p1==p2"<<endl;
    }
}


int main()
{
    test01();
    return 0;
}
```

### 4.5.6 函数调用运算符重载

1.函数调用运算符()也可以重载
2.由于重载后使用的方式非常像函数的调用，因此称为仿函数
3.仿函数没有固定写法，非常灵活


```C++
//函数调用运算符重载
class MyPring
{
public:
    //重载()运算符
    void operator()(string str)
    {
        cout<<"str="<<str<<endl;
    }
};

void MyPrint02(string str)
{
    cout<<"str="<<str<<endl;
}

void test01()
{
    MyPrint myPrint;
    myPrint("hello world"); //由于用起来非常类似函数的调用，因此称为仿函数

    MyPrint02("hello world");

}

///仿函数没有固定写法，非常灵活
class MyAdd
{
public:
    int operator()(int a,int b)
    {
        return a+b;
    }
};

void test02()
{
    MyAdd myadd;
    int res=myadd(10,20);
    cout<<"res="<<res<<endl;

    //匿名函数对象
    cout<<MyAdd()(100,200)<<endl;
}



int main()
{
    test01();
    return 0;
}


```



## 4.6 继承
继承是面向对象三大特性之一

### 4.6.1 继承的基本语法
```C++
//传统写法
class Java
{
public:
    void header()
    {
        cout<<"公共头部"<<endl;
    }

    void footer()
    {
        cout<<"公共底部区域"<<endl;
    }

    void left()
    {
        cout<<"公共分类列表"<<endl;
    }
    void content()
    {
        cout<<"Java内容区域"<<endl;
    }
};


class PYthon
{
public:
    void header()
    {
        cout<<"公共头部"<<endl;
    }

    void footer()
    {
        cout<<"公共底部区域"<<endl;
    }

    void left()
    {
        cout<<"公共分类列表"<<endl;
    }
    void content()
    {
        cout<<"PYthon内容区域"<<endl;
    }
};



class C++
{
public:
    void header()
    {
        cout<<"公共头部"<<endl;
    }

    void footer()
    {
        cout<<"公共底部区域"<<endl;
    }

    void left()
    {
        cout<<"公共分类列表"<<endl;
    }
    void content()
    {
        cout<<"C++内容区域"<<endl;
    }
};

void test1()
{
    cout<<"Java课程"<<endl;
    Java java;
    java.header();
    java.footer();
    java.left();
    java.content();
}

void test2()
{
    cout<<"PYthon课程"<<endl;
    PYthon pthon;
    pthon.header();
    pthon.footer();
    pthon.left();
    pthon.content();
}

void test3()
{
    cout<<"C++课程"<<endl;
    C++ cpp;
    cpp.header();
    cpp.footer();
    cpp.left();
    cpp.content();
}



int main()
{
    test1();
    test2();
    test3(); 
    return 0;
}


//继承写法

//好处：减少重复代码

//语法：
//子类名:继承方式 父类名
//{
//    子类成员函数
//};

//子类 也称为 派生类
//父类 也称为 基类

//公共页面类
class BasePage
{
public:
    void header()
    {
        cout<<"公共头部"<<endl;
    }

    void footer()
    {
        cout<<"公共底部区域"<<endl;
    }

    void left()
    {
        cout<<"公共分类列表"<<endl;
    }
};

//Java课程类
class JavaCourse:public BasePage
{
public:
    void content()
    {
        cout<<"Java内容区域"<<endl;
    }
};

//PYthon课程类
class PYthonCourse:public BasePage
{
public:
    void content()
    {
        cout<<"PYthon内容区域"<<endl;
    }
};

//C++课程类
class CPPCourse:public BasePage
{
public:
    void content()
    {
        cout<<"C++内容区域"<<endl;
    }
};

void test4()
{
    cout<<"Java课程"<<endl;
    JavaCourse java;
    java.header();
    java.footer();
    java.left();
    java.content();

    cout<<"PYthon课程"<<endl;
    PYthonCourse pthon;
    pthon.header();
    pthon.footer();
    pthon.left();
    pthon.content();

    cout<<"C++课程"<<endl;
    CPPCourse cpp;
    cpp.header();
    cpp.footer();
    cpp.left();
    cpp.content();
}

int main()
{
    test4();
    return 0;
}
 
```

### 4.6.2 继承方式

1.公有继承
2.私有继承
3.保护继承

```C++

class Base
{
public:
    int m_a;
protected:
    int m_b;
private:
    int m_c;
};

class Son1:public Base
{
public:
    void func()
    {
        m_a=100; //父类中的公有权限成员 到子类中依然是公有权限
        m_b=200; //父类中的保护权限成员 到子类中依然是保护权限

        //m_c=300; //父类中的私有权限成员 子类访问不到
    }
};

void test01()
{
    Son1 son1;
    son1.m_a=100; //公有权限成员 类外和类内都可以访问

    //son1.m_b=200; //错误，保护权限成员 类外不能访问，类内可以访问

}

//保护继承
class Base2
{
public:
    int m_a;
protected:
    int m_b;
private:
    int m_c;
};

class Son2:protected Base2
{
public:
    void func()
    {
        m_a=100; //父类中的公有权限成员 到子类中是保护权限
        m_b=200; //父类中的保护权限成员 到子类中是保护权限
        //m_c=300; //错误，父类中的私有权限成员 子类访问不到
    }
};

void test02()
{
    Son2 son2;
    //son2.m_a=100; //错误，保护权限成员 类外不能访问，类内可以访问

    son2.m_b=200; //保护权限成员 类外不可以访问，类内可以访问
}

//私有继承
class Base3
{
public:
    int m_a;
protected:
    int m_b;
private:
    int m_c;
};

class Son3:private Base3
{
public:
    void func()
    {
        m_a=100; //父类中的公有权限成员 到子类中是私有权限
        m_b=200; //父类中的保护权限成员 到子类中是私有权限
        //m_c=300; //错误，父类中的私有权限成员 子类访问不到
    }
};


void test03()
{
    Son3 son3;
    //son3.m_a=100; //错误，私有权限成员 类外不能访问，类内可以访问

    //son3.m_b=200; //私有权限成员 类外不可以访问，类内可以访问
}

class GrandSon:public Son3
{
public:
    void func()
    {
        //m_a=100; //错误，父类中的私有权限成员 到子类中是私有权限
        //m_b=200; //错误，父类中的私有权限成员 到子类中是私有权限
    }
};

int main()
{
    test01();
    return 0;
}

```


### 4.6.3 继承中的对象模型

/// 继承中的对象模型
```C++

class Base
{
public:
    int m_a;
protected:
    int m_b;
private:
    int m_c;
};


class Son1:public Base
{
public:
    int m_d;
}

//利用开发人员命令查看对象模型
//跳转盘符 
//跳转文件路径 cd 具体路径下
//查看命名
//cl /d1 reportSingleClassLayout类名 文件名

void test01()
{
    //父类所有非静态成员属性都会被子类继承下去
    //父类中私有成员属性，是被编译器隐藏起来的，子类中访问不到，但确实被继承下去了
    cout<<sizeof(Son1)<<endl; //16
}


int main()
{
    test01();
    return 0;
}

```


### 4.6.4 继承中构造和析构顺序

子类继承父类后，当创建子类对象，也会调用父类的构造函数


```C++

//继承中的构造和析构顺序
class Base
{
public:
    Base()
    {
        cout<<"Base()"<<endl;
    }
    ~Base()
    {
        cout<<"~Base()"<<endl;
    }
};

class Son:public Base
{
public:
    Son()
    {
        cout<<"Son()"<<endl;
    }
    ~Son()
    {
        cout<<"~Son()"<<endl;
    }
};


void test01()
{
    Base b;


    //继承中构造和析构顺序
    //先构造父类，再构造子类，析构的顺序与构造的顺序相反

    Son s; 
}


int main()
{

    return 0;
}


```


### 4.6.5 继承同名成员处理方式

问题：当子类与父类出现同名的成员，如何通过子类对象，访问到子类或父类中同名的数据呢?

1.访问子类同名成员，直接访问即可
2.访问父类同名成员，需要加作用域

```C++
class Base
{
public:
    Base()
    {
        m_a=100;
    }

    void func()
    {
        cout<<"Base::func()"<<endl;
    }

    void func(int a)
    {
        cout<<"Base::func(int a)"<<a<<endl;
    }

    int m_a;

};

class Son:public Base
{
public:
    Son()
    {
        m_a=200;
    }

    void func()
    {
        cout<<"Son::func()"<<endl;
    }

    

    int m_a;
};

void test01()
{
    Son son;
    cout<<son.m_a<<endl; //200
    //如果通过子类对象访问父类中的同名成员，需要加作用域
    cout<<son.Base::m_a<<endl; //100

    son.func();
    son.Base::func();

    //如果子类中出现和父类同名的成员函数，子类的同名成员函数会隐藏掉父类中所有同名成员函数
    //如果想访问到父类中被隐藏的同名成员函数，需要加作用域
    son.Base::func(100);
}

int main()
{
    test01();
    return 0;
}

```

总结：
1.子类对象可以直接访问到子类中同名成员
2.子类对象加作用域可以访问到父类中同名成员
3.当子类与父类拥有同名的成员函数，子类会隐藏父类中同名成员函数，加作用域可以访问到父类中同名函数


### 4.6.6 继承同名静态成员处理方式

问题：继承中同名的静态成员在子类对象上如何进行处理？

静态成员和非静态成员出现同名，处理方式一致

1.访问子类同名成员，直接访问即可
2.访问父类同名成员，需要加作用域

```C++
//继承同名静态成员处理方式
class Base
{
public:
    static int m_a;

    static void func()
    {
        cout<<"static Base::func()"<<endl;
    }

    static void func(int a)
    {
        cout<<"static Base::func(int a)"<<a<<endl;
    }
};

int Base::m_a=100;

class Son:public Base
{
public:
    static int m_a;

    static void func()
    {
        cout<<"static Son::func()"<<endl;
    }
};

int Son::m_a=200;

//同名静态成员属性
void test01()
{
    //1.通过对象访问
    Son s;
    cout<<"s.m_a="<<s.m_a<<endl; //200
    cout<<"s.Base::m_a="<<s.Base::m_a<<endl; //100

    //2.通过类名访问
    cout<<"Son::m_a="<<Son::m_a<<endl; //200

    //第一个::代表通过类名方式访问，第二个::代表访问父类作用域
    cout<<"Base::m_a="<<Son::Base::m_a<<endl; //100

}

//同名静态成员函数
void test02()
{
    //1.通过对象访问
    Son s;
    s.func();
    s.Base::func();

    //2.通过类名访问
    Son::func();
    Son::Base::func();

    Son::Base::func(100);
}


int main()
{

    return 0;
}

```


### 4.6.7 多继承语法

C++允许一个类继承多个类

语法：
class Son:public Base1,public Base2
{

};

多继承可能会引发父类中有同名成员函数出现，需要加作用域区分

```C++
//多继承语法

class Base1
{
public:
    Base1()
    {
        m_a=100;
    }

    int m_a;
};

class Base2
{
public:
    Base2()
    {
        m_a=200;
    }

    int m_a;
};

//子类 继承Base1和Base2
class Son:public Base1,public Base2
{
public:
    Son()
    {
        m_c=300;
        m_d=400;
    }

    int m_c;
    int m_d;
};

void test01()
{
    Son s;
    cout<< "sizeof(Son)="<<sizeof(Son)<<endl;

    cout<<"s.m_a="<<s.m_a<<endl; //100

    //当父类中出现同名成员，需要加作用域区分
    cout<<"s.Base1::m_a="<<s.Base1::m_a<<endl; //100
    cout<<"s.Base2::m_a="<<s.Base2::m_a<<endl; //200
}


int main()
{
    test01();
    return 0;
}


```

### 4.6.8 菱形继承

概念：
两个派生类继承同一个基类，又有第三个派生类继承这两个派生类，这种继承方式称为菱形继承，或者钻石继承

问题：
1.菱形继承可能会引发二义性问题，即子类对象访问到父类中同名成员时，需要加作用域区分
2.属性继承了多份，我们只需要一份数据


```C++
//菱形继承语法

//动物类
class Animal
{
public:
    int m_Age;
};

//利用虚继承 解决菱形继承问题
//继承之前 加上关键字 virtual 变为虚继承 
//Animal 类成为虚基类，Sheep类和Tuo类成为虚派生类
//羊类
class Sheep:virtual public Animal
{};

//驼类
class Tuo:virtual public Animal
{};

//羊驼类
class SheepTuo:public Sheep,public Tuo
{};


void test01()
{
    SheepTuo st;
    st.Sheepep::m_Age=18;
    st.Tuo::m_Age=28;

    cout<<"st.Sheepep::m_Age="<<st.Sheepep::m_Age<<endl; //18
    cout<<"st.Tuo::m_Age="<<st.Tuo::m_Age<<endl; //28

    //这份数据我们知道，但是我们只需要一份数据
    //解决方法：利用虚继承 解决菱形继承问题
    //继承之前 加上关键字 virtual 变为虚继承 
    //Animal 类成为虚基类，Sheep类和Tuo类成为虚派生类

    cout<<"st.m_Age="<<st.m_Age<<endl; //28
}


int main()
{
    test01();
    return 0;
}


```


## 4.7 多态

### 4.7.1 多态的基本概念

多态是C++面向对象三大特性之一

多态分为两类：
1.静态多态：函数重载和运算符重载属于静态多态，复用函数名
2.动态多态：派生类和虚函数实现运行时多态

静态多态和动态多态区别：
1.静态多态的函数地址早绑定 - 编译阶段确定函数地址
2.动态多态的函数地址晚绑定 - 运行阶段确定函数地址 


```C++

class Animal
{
public:
    //虚函数
    virtual void speak()
    {
        cout<<"动物在说话"<<endl;
    }
};

class Cat:public Animal
{
public:
    //重写 函数返回值类型 函数名 参数列表 完全相同 virtual关键字可写可不写 
    void speak()
    {
        cout<<"猫在说话"<<endl;
    }
}

class Dog:public Animal
{
public:
    void speak()
    {
        cout<<"狗在说话"<<endl;
    }
}


//执行说话函数
//C++中允许父类和子类之间类型转换，不需要强制类型转换，父类的指针和引用可以指向子类的对象
//地址早绑定，在编译阶段确定函数地址

//不管传递的是动物对象还是猫对象，都调用动物类的说话函数

//如果想要执行让猫说话，那么这个函数地址就不能早绑定，需要在运行阶段进行绑定，地址晚绑定
void doSpeak(Animal& animal)  //Animal& animal=cat
{
    animal.speak();//调用动物类的说话函数，而不是猫类的说话函数
}



void test01()
{
    Cat cat;
    doSpeak(cat);

    Dog dog;
    doSpeak(dog);
}

int main()
{
    test01();
    return 0;
}

/*
动态多态满足条件:
1.有继承关系
2.子类要重写父类的虚函数

动态多态使用：
父类的指针或者引用 指向子类对象 Animal& animal=cat
*/
```

### 4.7.2 多态案例一 ：计算器类

案例描述：
分别利用普通写法和多态技术，设计实现两个操作数进行运算的计算器类

多态的优点：
1.代码组织结构清晰
2.可读性强
3.利于前期和后期的扩展和维护

```C++

//普通写法
class Calculator
{
public:
    int getResult(string oper)
    {
        if (oper=='+')
        {
            return m_Num1+m_Num2;
        }
        else if (oper=='-')
        {
            return m_Num1-m_Num2;
        }
        else if (oper=='*')
        {
            return m_Num1*m_Num2;
        }
        //如果想扩展新的功能，需修改源码
        //在真实开发中 提倡 开闭原则
        //开闭原则：对扩展进行开放，对修改进行关闭
    }

    int m_Num1;
    int m_Num2;
};

void test01()
{
    Calculator c;
    c.m_Num1=10;
    c.m_Num2=5;
    cout<<c.m_Num1<<"+"<<c.m_Num2<<"="<<c.getResult("+")<<endl; //15

    cout<<c.m_Num1<<"-"<<c.m_Num2<<"="<<c.getResult("-")<<endl; //5

    cout<<c.m_Num1<<"*"<<c.m_Num2<<"="<<c.getResult("*")<<endl; //50

    
}


//多态写法
/*
多态使用条件：
1.有继承关系
2.子类要重写父类的虚函数

多态使用好处：
1.代码组织结构清晰
2.可读性强
3.利于前期和后期的扩展和维护

*/

//实现计算器抽象类

class AbstractCalculator
{
public:
    virtual int getResult()
    {
        return 0;
    }

    int m_Num1;
    int m_Num2;
};

//实现加法计算器类
class AddCalculator:public AbstractCalculator
{
public:
    int getResult()
    {
        return m_Num1+m_Num2;
    }
};

//实现减法计算器类
class SubCalculator:public AbstractCalculator
{
public:
    int getResult()
    {
        return m_Num1-m_Num2;
    }
};

//实现乘法计算器类
class MulCalculator:public AbstractCalculator
{
public:
    int getResult()
    {
        return m_Num1*m_Num2;
    }
};

void test02()
{
    //多态使用条件
    //父类指针或者引用指向子类对象

    //加法运算
    AddCalculator *abc=new AddCalculator;
    abc->m_Num1=10;
    abc->m_Num2=5;
    cout<<abc->m_Num1<<"+"<<abc->m_Num2<<"="<<abc->getResult()<<endl; //15

    //用完后，释放内存
    delete abc;

    //减法运算
    abc=new SubCalculator;
    abc->m_Num1=10;
    abc->m_Num2=5;
    cout<<abc->m_Num1<<"-"<<abc->m_Num2<<"="<<abc->getResult()<<endl; //5

    //用完后，释放内存
    delete abc;

    //乘法运算
    abc=new MulCalculator;
    abc->m_Num1=10;
    abc->m_Num2=5;
    cout<<abc->m_Num1<<"*"<<abc->m_Num2<<"="<<abc->getResult()<<endl; //50

    //用完后，释放内存
    delete abc;
}

int main()
{
    test01();
    test02();
    return 0;
}

```

### 4.7.3 纯虚函数和抽象类

在多态中，通常父类中虚函数的实现是毫无意义的，主要都是调用子类重写的内容

因此可以将虚函数改写为纯虚函数

纯虚函数语法：
``` C++
virtual 函数返回值类型 函数名 (参数列表) = 0;
```
当类中有了纯虚函数，这个类也称为抽象类

抽象类的特点：
1.无法实例化对象
2.子类必须重写抽象类中的纯虚函数，否则也属于抽象类


```C++

class Base
{
public:
    //纯虚函数
    //只要有一个纯虚函数，这个类成为抽象类
    //抽象类特点：
    //1.无法实例化对象
    //2.子类必须重写抽象类中的纯虚函数，否则也属于抽象类 
    virtual void func()=0;
};

class Son:public Base
{
public:
    virtual void func() 
    {
        cout<<"Son::func"<<endl;
    };
};


void test01()
{
    //无法实例化对象，因为是抽象类
    //Base b;    //错误，因为是抽象类，不能实例化对象
    //new Base;  //错误，因为是抽象类，不能实例化对象

    //子类对象
    Son s; //子类必须重写父类中的纯虚函数，否则无法实例化对象
    s.func();

    Base *base=new Son;
    base->func();
}




int main()
{
    test01();
    return 0;
}



```


### 4.7.4 多态案例二：制作饮品

案例描述：
制作饮品的流程为：煮水-冲泡-倒入杯中-加入辅料

利用多态技术实现本案例，提供抽象类制作饮品基类，提供子类制作咖啡和茶叶


```C++

class AbstractDrinking
{
public:
    //煮水
    virtual void boilWater()=0;

    //冲泡
    virtual void steep()=0;

    //倒入杯中
    virtual void pourInCup()=0;

    //加入辅料
    virtual void makeCondiments()=0;

    //制作饮品
    void makeDrink()
    {
        boilWater();
        steep();
        pourInCup();
        makeCondiments();
    }

};

//实现咖啡类
class Coffee:public AbstractDrinking
{
public:
    void boilWater()
    {
        cout<<"煮水"<<endl;
    }

    void steep()
    {
        cout<<"冲泡"<<endl;
    }

    void pourInCup()
    {
        cout<<"倒入杯中"<<endl;
    }

    void makeCondiments()
    {
        cout<<"加入糖和牛奶"<<endl;
    }
};



//实现茶叶类
class Tea:public AbstractDrinking
{
public:
    void boilWater()
    {
        cout<<"煮水"<<endl;
    }

    void steep()
    {
        cout<<"冲泡"<<endl;
    }

    void pourInCup()
    {
        cout<<"倒入杯中"<<endl;
    }

    void makeCondiments()
    {
        cout<<"加入柠檬汁"<<endl;
    }
};

void doWork(AbstractDrinking *drinking)
{
    drinking->makeDrink();
    //用完后，释放内存
    delete drinking;
}


void test01()
{
    doWork(new Coffee);

    doWork(new Tea);
}



int main()
{
    test01();
    return 0;
}

```

### 4.7.5 虚析构和纯虚析构

使用多态时，如果子类中有属性开辟到堆区，那么父类指针在释放时无法调用到子类的析构函数

解决方式：
将父类中析构函数设置为虚析构函数或者纯虚析构函数

虚析构和纯虚析构的共性：
1.可以解决父类指针释放子类对象
2.都需要有具体的函数实现


虚析构和纯虚析构的区别：
1.如果是纯虚析构，该类属于抽象类，无法实例化对象

虚析构语法：
virtual ~析构函数名(){}

纯虚析构语法：
virtual ~析构函数名()=0;
类名::~类名(){}



```C++


class Animal
{
public:
    Animal()
    {
        cout<<"Animal的构造函数"<<endl;
    }

    //利用虚析构可以解决 父类指针释放子类对象时不干净的问题
    virtual ~Animal()
    {
        cout<<"Animal的析构函数"<<endl;
    }

    //纯虚析构 需要生命也需要实现
    //有了纯虚析构，该类属于抽象类，无法实例化对象
    virtual ~Animal()=0;

    virtual void speak()=0;
};

Animal::~Animal()
{
    cout<<"Animal的纯虚析构函数"<<endl;
}

class Cat:public Animal
{
public:

    Cat(string name)
    {
        cout<<"Cat的构造函数"<<endl;
        m_Name=new string(name);
    }

    virtual void speak()
    {
        cout<<*m_Name<<"在说话"<<endl;
    }

    ~Cat()
    {
        if (m_Name!=NULL)
        {
            cout<<"Cat的析构函数"<<endl;
            delete m_Name;
            m_Name=NULL;
        }
    }

    string *m_Name;
};





void test01()
{
    Animal *animal=new Cat("Tom");
    animal->speak();
    //用完后，释放内存
    //父类指针在析构时，不会调用子类中的析构函数，导致子类如果有堆区属性，出现内存泄露
    delete animal;
}


int main()
{
    test01();
    return 0;
}


```

总结：
1.虚析构和纯虚析构就是用来解决通过父类指针释放子类对象时不干净的问题
2.如果子类中没有多去数据，可以不写虚析构或纯虚析构
3.有了纯虚析构，该类属于抽象类，无法实例化对象，纯虚析构 需要生命也需要实现

###  4.7.6 多态案例三：电脑组装

案例描述：
电脑主要组成部件为CPU（用于计算）、内存（用于存储数据）、显卡（用于显示图像）
将每个零件封装出抽象基类，并且提供不同的厂商生产不同的零件类，例如：Intel厂商，AMD厂商，NVIDIA厂商，ATI厂商等
创建电脑类提供让电脑工作的函数，并且调用每个零件工作的接口
测试是组装三台不同的电脑进行工作

```C++
class CPU
{
public:
    virtual void calculate()=0;
};

class Memory
{
public:
    virtual void store()=0;
};

class GPU
{
public:
    virtual void display()=0;
};

class Computer
{
public:
    Computer(CPU *cpu,Memory *memory,GPU *gpu)
    {
        m_cpu=cpu;
        m_memory=memory;
        m_gpu=gpu;

    }

    ~Computer()
    {
        if(m_cpu!=NULL)
        {
            delete m_cpu;
            m_cpu=NULL;
        }
        if(m_memory!=NULL)
        {
            delete m_memory;
            m_memory=NULL;
        }
        if(m_gpu!=NULL)
        {
            delete m_gpu;
            m_gpu=NULL;
        }
    }

    void work()
    {
        m_cpu->calculate();
        m_memory->store();
        m_gpu->display();
    }

private:

    CPU * m_cpu;
    Memory * m_memory;
    GPU * m_gpu;

};

class intelCPU:public CPU
{
public:
    void calculate()
    {
        cout<<"IntelCPU开始计算"<<endl;
    }
};

class amdCPU:public CPU
{
public:
    void calculate()
    {
        cout<<"AMD CPU开始计算"<<endl;
    }
};

class nvidiaGPU:public GPU
{
public:
    void display()
    {
        cout<<"NVIDIA GPU开始显示"<<endl;
    }
};

class atiGPU:public GPU
{
public:
    void display()
    {
        cout<<"ATI GPU开始显示"<<endl;
    }
};

class SKMemory:public Memory
{
public:
    void store()
    {
        cout<<"SK内存开始存储"<<endl;
    }
};

class MeiguangMemory:public Memory
{
public:
    void store()
    {
        cout<<"Meiguang内存开始存储"<<endl;
    }
};

void test01()
{
    CPU* cpu=new intelCPU();
    Memory* memory=new SKMemory();
    GPU* gpu=new nvidiaGPU();
    Computer* computer=new Computer(cpu,memory,gpu);
    computer->work();
    delete computer;
    
}

int main()
{
    test01();
    return 0;
}

```




# 5.文件操作
程序运行是产生的临时文件，程序一旦运行结束就会被释放

**==通过文件可以将数据持久化==**

C++中对文件操作需要包含头文件<fstream.h>

文件类型分为两种：
1.文本文件：文件以文本的ASCII码存储，例如：.txt,.doc,.docx,.pdf等
2.二进制文件：文件以二进制的形式存储，例如：.exe,.dll,.sys等


操作文件三大类：
1.ostream:输出流类，用于将数据写入文件
2.istream:输入流类，用于从文件中读取数据
3.fstream:流类，用于对文件进行读写操作，是ostream和istream的派生类


## 5.1.文本文件

### 5.1.1.写文件

写文件步骤如下：
1.包含头文件   
#include<fstream.h>

2.创建文件对象
ofstream ofs("test.txt");

3.打开文件
ofs.open("文件路径",打开方式);

4.写入数据
ofs<<"写入数据";

5.关闭文件
ofs.close();

文件打开方式

|打开方式|解释|
|--|--|
|ios::in|为读文件而打开文件|
|ios::out|为写文件而打开文件|
|ios::ate|初始位置：文件尾|
|ios::app|追加方式写文件|
|ios::trunc|如果文件存在先删除，在创建|
|ios::binary|二进制方式|

注意：文件打开方式可以配合使用，利用|操作符
例如：利用二进制方式写文件 
ofs.open("文件路径",ios::out|ios::binary);

```C++
#include<fstream.h>

//文本文件 写文件
void test01()
{
    //1.包含头文件

    //2.创建文件对象
    ofstream ofs;

    //3.指定打开方式
    ofs.open("test.txt",ios::out);

    //4.写入数据
    ofs<<"姓名：张三"<<endl;
    ofs<<"年龄：18"<<endl;
    ofs<<"性别：男"<<endl;

    //5.关闭文件
    ofs.close();

}

```

总结：
1.文件操作需要包含头文件<fstream.h>
2.读文件可以利用ofstream，或者fstream类
3.打开文件时需要指定操作文件的路径，以及打开方式
4.利用<<可以向文件中写数据
5.操作完毕，要关闭文件

### 5.1.2 读文件

读文件步骤如下：
1.包含头文件   
#include<fstream.h>

2.创建文件对象
ifstream ifs;

3.打开文件并判断文件是否打开成功
ifs.open("文件路径",打开方式);

4.读取数据
四种读取方式

5.关闭文件
ifs.close();

```C++
#include<fstream.h>
#include<string>
//文本文件 读文件
void test01()
{
    //1.包含头文件
    // #include<fstream.h>

    //2.创建文件对象
    ifstream ifs;

    //3.打开文件并判断文件是否打开成功
    ifs.open("test.txt",ios::in);

    if (! ifs.is_open())
    {
        cout<<"文件打开失败"<<endl;
        return;
    }

    //4.读取数据
    
    //第一种
    char buf[1024]={0};
    while(ifs >> buf)
    {
        cout<<buf<<endl;
    }

    //第二种
    char buf[1024]={0};
    while(ifs.getline(buf,sizeof(buf)))
    {
        cout<<buf<<endl;
    }

    //第三种
    string buf;
    while(getline(ifs,buf)) //参数：文件流对象，字符串对象
    {
        cout<<buf<<endl;
    }

    //第四种
    char c;
    while((c=ifs.get())!=EOF) //EOF end of file
    {
        cout<<c<<endl;
    }

    //5.关闭文件
    ifs.close();


}


int main()
{
    return 0;
}


```


### 5.2 二进制文件

以二进制的方式对文件进行读写操作
打开方式指定为ios::binary

### 5.2.1 写二进制文件

二进制方式写文件主要利用流对象调用成员函数write
函数原型：
ostream& write(const char*  buffer,int len);

参数解释：字符指针buffer指向内存中一段储存空间，len是读写的字节数

```C++
#include<fstream.h>
#include<string>
//二进制文件 写文件

class Person
{
public:
    char m_Name[10];
    int m_Age;
};


void test01()
{
    //1.包含头文件
    // #include<fstream.h>

    //2.创建文件对象
    ofstream ofs;
    //ofstream ofs("Person.txt",ios::out|ios::binary)

    //3.指定打开方式
    ofs.open("Person.txt",ios::out|ios::binary);

    //4.写入数据
    Person p={"张三",18};
    ofs.write((const char *)& p,sizeof(Person));
    //&p -- 类型是Person，需要强制类型转换为const char*

    //5.关闭文件
    ofs.close();
}

int main()
{
    test01();
    return 0;
}

```

### 5.2.2 读二进制文件

二进制方式读文件主要利用流对象调用成员函数read
函数原型：
istream& read(char* buffer,int len);

函数参数解释：
字符指针buffer指向内存中一段储存空间，len是读写的字节数

```C++
#include<fstream.h>

#include<string>
//二进制文件 读文件
class Person
{
public:
    char m_Name[10];
    int m_Age;

};

void test01()
{
    //1.包含头文件
    // #include<fstream.h>

    //2.创建文件对象
    ifstream ifs;

    //3.打开文件并判断文件是否打开成功
    ifs.open("Person.txt",ios::in|ios::binary);

    if (! ifs.is_open())
    {
        cout<<"文件打开失败"<<endl;
        return;
    }

    //4.读取数据
    Person p;
    ifs.read((char *)& p,sizeof(Person));
    cout<<"姓名："<<p.m_Name<<endl;
    cout<<"年龄："<<p.m_Age<<endl;

    //5.关闭文件
    ifs.close();
}


int main()
{
    test01();
    return 0;
}

```






