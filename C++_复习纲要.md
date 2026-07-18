# C++ 期末复习纲要

> 基于你的笔记 + 考试重点整理
> 重点内容（考试高频点）已用 **加粗** 标记
> 核心关键词：virtual / typename / explicit / override / const / static / friend / template / virtual public / operator

---

## 📚 目录

- 第 1 章：引用（Reference）
- 第 2 章：函数提高（默认参数 / 占位参数 / 重载）
- 第 3 章：类和对象（封装 / 构造析构 / 深浅拷贝 / 静态成员 / this / const / 友元 / 运算符重载）
- 第 4 章：继承（方式 / 对象模型 / 构造析构顺序 / 同名成员 / 多继承 / 菱形继承 / 虚继承）
- 第 5 章：多态（虚函数 / 纯虚函数 / 抽象类 / 虚析构）
- 第 6 章：文件操作（文本/二进制 + IO流格式化输出）
- 第 7 章：模板（函数模板 / 类模板）
- 第 8 章：STL 初识（容器/算法/迭代器 + vector）
- 附录 A：自测题参考答案

---

# 第 1 章 引用（Reference）

## 1.1 核心语法速查表

```cpp
int a = 10;
int& ref = a;        // 引用：给a起别名
ref = 20;            // 改ref就是改a
```

**必背关键词**：`&`（引用符号）、**引用必须初始化**、**引用一旦绑定不可改**

## 1.2 "是什么 vs 为什么"

- **是什么**：引用是变量的别名，**在C++内部实现是一个指针常量**（`T* const`），所有指针操作由编译器代劳。
- **为什么用**：函数传参时简化指针修改实参的写法；避免值拷贝；返回值可作为左值。

## 1.3 易错点与高频陷阱

- ⚠️ **不要返回局部变量的引用**（函数结束栈区销毁，引用指向野内存）
- ⚠️ 引用做函数返回值时，若要支持链式赋值 `test()=100`，**必须返回引用** `int&`
- ⚠️ `const int& a = 10;` 是合法的（常量引用可以指向临时量），但 `int& a = 10;` 非法

## 1.4 极简代码示例

```cpp
// 引用做函数参数（简化指针版）
void swap(int& a, int& b) { // a/b是实参的别名
    int t = a; a = b; b = t;
}
int x=1, y=2;
swap(x, y);  // 直接传，不需要取地址
```

## 1.5 自测小问答

**Q1**：下面代码能编译通过吗？为什么？
```cpp
int& func() {
    int a = 10;
    return a;
}
```
<details><summary>参考答案</summary>不能。返回了**局部变量**的引用，函数结束后a被销毁，引用成为**野引用**，使用会引发未定义行为。</details>

---

# 第 2 章 函数提高

## 2.1 默认参数

### 语法速查

```cpp
int func(int a, int b = 10, int c = 20) {  // 默认参数必须靠右
    return a + b + c;
}
func(1);       // 1+10+20 = 31
func(1, 2);    // 1+2+20 = 23
```

### 易错点

- ⚠️ **声明和实现只能有一个提供默认参数**（通常在声明里给）
- ⚠️ 默认参数必须**从右往左连续**，不能跳跃

## 2.2 占位参数

```cpp
void func(int a, int) {  // 第二个int是占位参数
    cout << a;
}
func(10, 20);  // 必须传两个参数
```

## 2.3 函数重载 ⭐ 考试高频

### 满足条件（同时满足）

1. **同一个作用域**
2. 函数名相同
3. 参数列表不同（**类型 / 个数 / 顺序** 至少一个不同）

### ❌ 易错点（必考）

| 情况 | 是否构成重载 |
|------|------------|
| 参数类型不同 | ✅ 是 |
| 参数个数不同 | ✅ 是 |
| 参数顺序不同 | ✅ 是 |
| **仅返回值不同** | ❌ 否 |
| 形参 const 不同（值传递） | ❌ 否 |
| 形参 `int&` vs `const int&` | ✅ 是（**引用有无const**算不同） |

### 高频坑：重载 + 默认参数 → 二义性

```cpp
void func(int a, int b = 10) {}
void func(int a) {}
func(10);   // ❌ 编译错误：二义性，两个都能调
```

### 引用作为重载条件

```cpp
void func(int& a) {}      // 只能传变量
void func(const int& a) {}// 可传变量或字面量
int x = 10;
func(x);      // 调第一个
func(10);     // 调第二个（10是常量，只能绑const引用）
```

## 2.4 极简代码示例

```cpp
// 函数重载：同名不同参
int add(int a, int b) { return a + b; }         // 整型
double add(double a, double b) { return a + b; } // 浮点
cout << add(1, 2) << endl;      // 3
cout << add(1.1, 2.2) << endl;  // 3.3
```

## 2.5 自测小问答

**Q1**：以下两函数能否构成重载？为什么？
```cpp
void func(int a) {}
int  func(int a) { return a; }
```
<details><summary>参考答案</summary>不能。**仅返回值类型不同不能构成重载**（调用时编译器无法区分你要哪个）。</details>

---

# 第 3 章 类和对象

## 3.1 三大特性：封装 / 继承 / 多态 ⭐⭐⭐

## 3.2 封装

### 3.2.1 访问权限

| 修饰符 | 类内 | 类外 | 派生类 |
|--------|------|------|--------|
| **public** | ✅ | ✅ | ✅ |
| **protected** | ✅ | ❌ | ✅ |
| **private** | ✅ | ❌ | ❌ |

### 3.2.2 struct vs class

> **唯一区别**：默认访问权限不同
> - `struct` 默认 **public**
> - `class` 默认 **private**

### 3.2.3 成员属性私有化的优点

1. 可自己控制读写权限（提供 public 的 get/set）
2. 可在 set 中**监测数据有效性**（如：年龄不能为负）

## 3.3 构造函数与析构函数 ⭐⭐⭐

### 3.3.1 构造函数

```cpp
class Person {
public:
    Person() {}                      // 无参构造（默认构造）
    Person(int a) { age = a; }       // 有参构造
    Person(const Person& p) { ... }  // 拷贝构造
};
```

**特征**：
- 没有返回值，不写 `void`
- 函数名 = 类名
- **可以有参数，可重载**
- 对象创建时**自动调用一次**

### 3.3.2 析构函数

```cpp
~Person() {}
```

**特征**：
- 没有返回值，不写 `void`
- 函数名 = `~类名`
- **不能有参数，不能重载**
- 对象销毁前**自动调用一次**

### 3.3.3 三种调用方法

```cpp
Person p1;             // 括号法：默认构造
Person p2(10);         // 括号法：有参构造
Person p3(p2);         // 括号法：拷贝构造
Person p4 = Person(10);// 显式法
Person p5 = 10;        // 隐式转换法 → 相当于 Person(10)
Person p6 = p5;        // 隐式转换法 → 拷贝构造
```

### ❌ 易错点

```cpp
Person p();  // ❌ 编译器认为这是函数声明，不是对象创建
```

### 3.3.4 拷贝构造调用时机（3 种）

1. 用已创建对象初始化新对象：`Person p2(p1);`
2. 值传递函数参数：`void func(Person p)` → 实参传给形参时
3. 值方式返回局部对象

### 3.3.5 构造/析构调用规则（编译器默认行为）

| 你写的 | 编译器补的 |
|--------|----------|
| 啥也没写 | 默认无参构造 + 默认析构 + 默认拷贝构造（**值拷贝**） |
| 自定义有参构造 | 不再提供默认无参构造，但**仍提供默认拷贝构造** |
| 自定义拷贝构造 | **不再提供其他普通构造函数** |

## 3.4 深拷贝 vs 浅拷贝 ⭐⭐⭐ 考试必考

### 概念

- **浅拷贝**：简单的赋值拷贝（编译器默认行为）
- **深拷贝**：在**堆区重新申请空间**进行拷贝

### 问题场景

```cpp
class Person {
public:
    int* m_Age;
    Person(int age) { m_Age = new int(age); }
    ~Person() { if (m_Age) delete m_Age; }  // 析构释放堆区
};
Person p1(18);
Person p2(p1);  // 浅拷贝：p2.m_Age 与 p1.m_Age 指向同一块内存
// 析构时：p2 先 delete，然后 p1 再 delete 同一块 → 重复释放崩溃
```

### 解法：深拷贝

```cpp
Person(const Person& p) {
    m_Age = new int(*p.m_Age);  // 重新申请空间
}
```

### 一句话总结

> **有指针成员 / 堆区数据 → 必须自己写拷贝构造 + operator=（深拷贝）**

## 3.5 初始化列表 ⭐

```cpp
class Person {
public:
    int m_A, m_B;
    Person(int a, int b) : m_A(a), m_B(b) {}  // 初始化列表
};
```

**作用**：比函数体内赋值更高效（避免先默认构造再赋值），**且是 const 成员、引用成员、对象成员唯一能被初始化的方式**。

## 3.6 类对象作为类成员

```cpp
class Phone { /*...*/ };
class Person {
    string m_Name;
    Phone   m_Phone;   // 类对象成员
};
```

**构造顺序**：先构造**对象成员**（Phone），再构造**自身**（Person）
**析构顺序**：与构造**相反**（先析构 Person，再析构 Phone）

## 3.7 静态成员 ⭐⭐

### 静态成员变量

```cpp
class Person {
public:
    static int m_A;  // 类内声明
private:
    static int m_B;
};
int Person::m_A = 100;  // ⚠️ 类外初始化（必须有）
```

**特点**：
- **所有对象共享同一份数据**
- 编译阶段分配内存
- 类内声明，**类外必须初始化**
- 访问方式：`对象.m_A` 或 `Person::m_A`

### 静态成员函数

```cpp
static void func() { m_A = 100; /* m_B 错误 */ }
```

**特点**：
- 所有对象共享同一个函数
- **只能访问静态成员变量**（无 this 指针）

## 3.8 this 指针 ⭐⭐

### 本质

- **指向被调用的成员函数所属的对象**
- 隐含在每个**非静态**成员函数中
- 本质是**指针常量** `Person* const this`，**指向不可改**

### 用途（两大场景）

1. **区分形参和成员变量同名**
   ```cpp
   Person(int age) { this->age = age; }  // this->age 是成员
   ```

2. **链式调用返回对象本身**
   ```cpp
   Person& PersonAddAge(Person& p) {
       this->age += p.age;
       return *this;   // 返回自身引用，才能链式
   }
   p2.PersonAddAge(p1).PersonAddAge(p1);  // 链式
   ```

### ⚠️ 易错点：空指针访问成员函数

```cpp
Person* p = nullptr;
p->ShowClassName();   // ✅ 不涉及 this 解引用，可以
p->showAge();         // ❌ 函数内部访问 m_Age → 相当于 this->m_Age → 空指针解引用崩溃
```

**解法**：函数入口加 `if (this == nullptr) return;`

## 3.9 const 修饰成员函数（常函数）

```cpp
void showPerson() const {  // 修饰 this 指针：const Person* const this
    m_A = 100;  // ❌ this 指向的值不可改
    m_B = 100;  // ✅ mutable 修饰的特殊变量可以改
}
```

**记忆口诀**：
- 函数后加 `const` → **常函数**，不能修改成员属性
- 成员声明加 `mutable` → 在常函数中也能改
- 对象前加 `const` → **常对象**，**只能调用常函数**

## 3.10 友元（friend）⭐

**目的**：让类外特殊函数/类访问本类的 private 成员

**三种实现**：

```cpp
// 1. 全局函数做友元
friend void goodGay(Building* b);

// 2. 另一个类做友元
friend class GoodGay;

// 3. 另一个类的成员函数做友元
friend void GoodGay::visit();
```

## 3.11 运算符重载 ⭐⭐⭐ 必考大题

### 3.11.1 是什么

- 对已有运算符重新定义，赋予另一种功能
- 本质是**函数**

### 3.11.2 加号 + 重载

```cpp
class Person {
public:
    int a, b;
    // 成员函数重载：p1.operator+(p2) 简化 p1+p2
    Person operator+(Person& p) {
        Person t; t.a = a + p.a; t.b = b + p.b; return t;
    }
};
// 全局函数版：operator+(p1, p2)
```

### 3.11.3 左移 << 重载（必考）

```cpp
// ⚠️ 不能用成员函数重载 <<，因为 cout 在左侧，成员函数 this 在左侧
// 必须用全局函数 + 友元访问 private
class Person {
    friend ostream& operator<<(ostream& cout, Person& p);
private:
    int a, b;
};
ostream& operator<<(ostream& cout, Person& p) {
    cout << "a=" << p.a << " b=" << p.b;
    return cout;  // ⚠️ 必须返回 ostream& 才能链式 (cout << p << endl;)
}
```

### 3.11.4 递增 ++ 重载（区分前后置）⭐

```cpp
class MyInt {
    int num;
public:
    // 前置++：先++后返回
    MyInt& operator++() {       // 返回引用 → 一直对一个数操作
        ++num;
        return *this;
    }
    // 后置++：先记录原值再++，返回原值
    MyInt operator++(int) {     // int 是占位参数，用于区分前后置
        MyInt temp = *this;
        ++num;
        return temp;            // 返回值（不是引用）
    }
};
```

**记忆口诀**：
- 前置 `++a`：**先加后返** → 返回**引用**
- 后置 `a++`：**先返后加** → 返回**值**（`int` 占位区分）

### 3.11.5 赋值 = 重载（深拷贝点）

> **C++ 编译器默认给类添加 4 个函数**：
> 1. 默认构造  2. 默认析构  3. 默认拷贝构造  4. **默认 operator=**

```cpp
class Person {
    int* m_Age;
public:
    Person(int age) { m_Age = new int(age); }
    ~Person() { if (m_Age) delete m_Age; m_Age = nullptr; }
    
    Person& operator=(Person& p) {  // 必须返回引用支持 p3=p2=p1
        if (this != &p) {            // 自我赋值检查
            if (m_Age) { delete m_Age; m_Age = nullptr; }  // 先释放旧内存
            m_Age = new int(*p.m_Age);  // 深拷贝
        }
        return *this;
    }
};
```

### 3.11.6 函数调用 () 重载（仿函数）

```cpp
class MyPrint {
public:
    void operator()(string s) { cout << s; }
};
MyPrint()("hello");  // 匿名对象调用
```

**特点**：写法灵活无固定格式，使用方式像函数调用，所以叫**仿函数**。

## 3.12 类与对象 极简示例

```cpp
class Person {
    string name;
    int age;
public:
    Person(string n, int a) : name(n), age(a) {}  // 初始化列表
    void show() { cout << name << ":" << age; }
};
Person p("Tom", 18);  // 调用构造函数
p.show();
```

## 3.13 类与对象 自测题

**Q1**：下面代码有什么问题？如何修复？
```cpp
class Person {
    int* age;
public:
    Person(int a) { age = new int(a); }
    ~Person() { delete age; }
};
Person p1(18);
Person p2(p1);
```
<details><summary>参考答案</summary>**浅拷贝问题**：p1 和 p2 的 age 指向同一块堆区，析构时**重复 delete 崩溃**。**修复**：自定义**拷贝构造函数**做深拷贝：<code>Person(const Person& p) { age = new int(*p.age); }</code></details>

**Q2**：`if (p1 == p2)` 想比较两个 Person 对象，应该怎么实现？
<details><summary>参考答案</summary>**重载 == 运算符**：作为成员函数 <code>bool operator==(Person& p) { return name==p.name && age==p.age; }</code></details>

---

# 第 4 章 继承 ⭐⭐⭐

## 4.1 基本语法

```cpp
// 父类 / 基类
class BasePage { public: void header(); /*...*/ };

// 子类 / 派生类
class Java : public BasePage {  // ⚠️ 继承方式
public:
    void content();
};
```

**意义**：减少重复代码。

## 4.2 三种继承方式 ⭐⭐⭐ 必考

| 父类成员 \ 继承方式 | public 继承 | protected 继承 | private 继承 |
|------------------|------------|---------------|--------------|
| public | **public** | protected | private |
| protected | **protected** | protected | private |
| private | 不可见 | 不可见 | 不可见 |

**记忆口诀**：
- public 继承：**不改权限**
- protected 继承：**全部降为 protected**（最高降到 protected）
- private 继承：**全部降为 private**（最高降到 private）
- 父类 private：**任何继承方式下子类都不可访问**（但其实**被继承下来了**，只是被隐藏）

## 4.3 继承中的对象模型

- 父类**所有非静态成员属性**都会被子类继承
- 父类中 private 成员**被编译器隐藏**，访问不到但**确实占空间**
- `sizeof(子类) = 父类所有成员 + 子类新增成员`

> 查看对象模型命令（VS Developer Command Prompt）：
> `cl /d1 reportSingleClassLayout类名 文件名.cpp`

## 4.4 继承中构造/析构顺序 ⭐⭐

> **先构造父，再构造子；先析构子，再析构父**（与构造相反）

```
Base()  →  Son()  →  ...使用...  →  ~Son()  →  ~Base()
```

## 4.5 同名成员处理

```cpp
class Base { public: int m_A = 100; };
class Son  : public Base { public: int m_A = 200; };

Son s;
s.m_A;          // 200（子类）
s.Base::m_A;    // 100（父类，加作用域）
```

**同名成员函数**：子类同名函数**隐藏**父类所有同名函数（不管参数），想访问父类版本必须加作用域。

```cpp
Son s;
s.func();         // 子类
s.Base::func(10); // 父类带参版（被隐藏，需加作用域）
```

**静态成员同名处理同上**：
- 通过对象访问：`s.Base::m_A`
- 通过类名访问：`Son::Base::m_A`（**两个 `::`**）

## 4.6 多继承

```cpp
class Son : public Base1, public Base2 {};
```

**问题**：父类出现同名成员时**二义性**，需加作用域区分。
**实际开发中不建议使用**（设计复杂、易歧义）。

## 4.7 菱形继承 ⭐⭐ 难点

### 问题

```
        Animal
        /    \
     Sheep   Tuo
        \    /
       SheepTuo
```

- 继承了两份 `m_Age`，数据冗余
- 访问 `st.m_Age` **二义性**

### 解决：虚继承

```cpp
class Animal { public: int m_Age; };

class Sheep : virtual public Animal {};  // ⚠️ virtual
class Tuo   : virtual public Animal {};  // ⚠️ virtual

class SheepTuo : public Sheep, public Tuo {};
// Animal 称为 虚基类
// Sheep/Tuo 称为 虚派生类
// 此时 SheepTuo 中 m_Age 只有一份
```

**核心**：加 `virtual` 之后，最顶层的父类数据在子类中**只有一份**（通过虚基类指针 vbptr 间接访问）。

## 4.8 继承 极简示例

```cpp
class Animal { public: void eat() { cout << "eat"; } };
class Dog : public Animal { public: void bark() { cout << "bark"; } };
Dog d;
d.eat();    // 继承自父类
d.bark();   // 子类自己的
```

## 4.9 继承 自测题

**Q1**：父类 public 成员，private 继承后在子类内的访问权限是？
<details><summary>参考答案</summary>private（父类 public → private 继承后**降为 private**）。</details>

**Q2**：菱形继承中两个父类都有同名成员 `m_A`，子类对象 `st.m_A` 访问是否合法？怎么办？
<details><summary>参考答案</summary>不合法，**二义性**。两种方案：① 加作用域 <code>st.Sheep::m_A</code>；② 用**虚继承** <code>virtual public Animal</code> 使数据只有一份。</details>

---

# 第 5 章 多态 ⭐⭐⭐ 必考

## 5.1 静态多态 vs 动态多态

| 类型 | 实现方式 | 函数地址 |
|------|---------|---------|
| **静态多态** | 函数重载、运算符重载 | **早绑定**（编译阶段） |
| **动态多态** | **派生类 + 虚函数** | **晚绑定**（运行阶段） |

## 5.2 动态多态条件（背下来）⭐⭐⭐

> 三个条件缺一不可：
> 1. 有**继承关系**
> 2. 子类**重写**父类的**虚函数**
> 3. 用**父类的指针或引用**指向子类对象

### 重写 vs 重载（对比记忆）

| 维度 | 重写 (override) | 重载 (overload) |
|------|----------------|----------------|
| 位置 | 父子类之间 | 同一作用域 |
| 函数名 | 必须相同 | 必须相同 |
| 参数列表 | **必须完全相同** | 必须不同 |
| virtual | 父类必须有 virtual | 无关 |
| 返回值 | 一般相同（协变除外） | 无关 |

## 5.3 虚函数

```cpp
class Animal {
public:
    virtual void speak() {  // ⚠️ virtual 关键字
        cout << "动物叫";
    }
};
class Cat : public Animal {
public:
    void speak() override {  // 重写父类，virtual 可省略
        cout << "猫叫";
    }
};
void doSpeak(Animal& a) { a.speak(); }  // 父类引用指向子类对象
Cat c;
doSpeak(c);  // 输出"猫叫"——运行时多态
```

**没有 `virtual`**：永远调用 Animal 版的 speak（早绑定）。

## 5.4 纯虚函数 & 抽象类 ⭐⭐⭐

### 语法

```cpp
virtual 函数返回值类型 函数名(参数列表) = 0;  // = 0 即纯虚
```

### 抽象类特点

1. **无法实例化对象**（`Base b;` ❌ / `new Base;` ❌）
2. 子类**必须重写**抽象类中的纯虚函数，否则子类也是抽象类

## 5.5 虚析构 & 纯虚析构 ⭐⭐

### 解决的问题

> 多态下，**父类指针释放子类对象**时，**不会调用子类的析构函数** → 子类堆区数据泄漏

### 解决

```cpp
// 1. 虚析构
virtual ~Animal() {}

// 2. 纯虚析构（需要声明 + 类外实现）
virtual ~Animal() = 0;
Animal::~Animal() {}  // ⚠️ 必须有实现
```

| | 虚析构 | 纯虚析构 |
|--|--------|---------|
| 能否解决父类指针释放子类对象 | ✅ | ✅ |
| 类是否变成抽象类 | ❌ | ✅（无法实例化）|
| 需不需要实现 | 不需要 | **必须有实现**（类外） |

## 5.6 多态 极简示例

```cpp
class Shape {  // 抽象类
public:
    virtual double area() = 0;  // 纯虚函数
};
class Circle : public Shape {
    double r;
public:
    Circle(double x):r(x){}
    double area() override { return 3.14*r*r; }  // 重写
};
Shape* s = new Circle(2.0);
cout << s->area();  // 12.56
delete s;  // ⚠️ Shape 中需有虚析构，否则子类的析构不调用
```

## 5.7 多态 自测题

**Q1**：什么是多态？动态多态需要满足哪几个条件？
<details><summary>参考答案</summary>同一接口表现出不同行为。条件：① 继承关系 ② 子类重写父类**虚函数** ③ **父类指针或引用**指向子类对象。</details>

**Q2**：多态下父类指针 `delete` 子类对象会怎样？怎么解决？
<details><summary>参考答案</summary>只调用父类析构，**子类析构不调用**（若子类有堆区数据则泄漏）。解决：父类析构改为**虚析构**或**纯虚析构**。</details>

---

# 第 6 章 文件操作

## 6.1 文件类型与三大类

| 类型 | 说明 |
|------|------|
| 文本文件 | ASCII 存储（.txt .cpp） |
| 二进制文件 | 二进制存储（.exe .jpg） |

| 类 | 作用 |
|----|------|
| ofstream | 写 |
| ifstream | 读 |
| fstream | 读写（ofstream/ifstream 的基类） |

## 6.2 打开方式（必背）

| 标志 | 含义 |
|------|------|
| `ios::in` | 读 |
| `ios::out` | 写 |
| `ios::ate` | 初始位置：文件尾 |
| `ios::app` | 追加写 |
| `ios::trunc` | 文件存在先删再建 |
| `ios::binary` | 二进制 |

组合用 `|`：`ios::out | ios::binary`

## 6.3 文本文件写

```cpp
#include <fstream>
ofstream ofs;
ofs.open("test.txt", ios::out);
ofs << "hello" << endl;
ofs.close();
```

## 6.4 文本文件读（四种方式）

```cpp
ifstream ifs("test.txt", ios::in);
if (!ifs.is_open()) { return; }

// 方式1：>> 运算符
char buf[1024]; while (ifs >> buf) cout << buf;

// 方式2：getline 成员
while (ifs.getline(buf, sizeof(buf))) cout << buf;

// 方式3：全局 getline
string s; while (getline(ifs, s)) cout << s;

// 方式4：单字符 get
char c; while ((c = ifs.get()) != EOF) cout << c;
```

## 6.5 二进制文件

```cpp
// 写
ofstream ofs("p.bin", ios::out | ios::binary);
Person p = {"Tom", 18};
ofs.write((const char*)&p, sizeof(p));  // 强转 const char*
ofs.close();

// 读
ifstream ifs("p.bin", ios::in | ios::binary);
Person p;
ifs.read((char*)&p, sizeof(p));
```

## 6.6 IO 流格式化输出 ⭐ 考试重点

> 考试明确要求：**输出左对齐右对齐使用 IO 流**

需要头文件 `<iomanip>`：

| 操纵符 | 作用 |
|--------|------|
| `setw(n)` | 设置**字段宽度**（默认**右对齐**） |
| `setiosflags(ios::left)` | **左对齐** |
| `setiosflags(ios::right)` | 右对齐（默认） |
| `setfill(c)` | 设置填充字符 |
| `setprecision(n)` | 设置浮点数精度 |
| `fixed` + `setprecision(n)` | 定点小数 n 位 |

### 极简示例

```cpp
#include <iomanip>
cout << setw(8) << setiosflags(ios::left) << "Tom" << setw(5) << 18 << endl;
// 输出："Tom     18   "（左对齐，宽度8和5）
cout << setw(8) << setiosflags(ios::right) << "Tom" << endl;
// 输出："     Tom"（右对齐，宽度8，空格填充）
```

### 易错点

- `setw` **只对紧跟的一个输出有效**
- 默认对齐方式是**右对齐**

## 6.7 文件操作 自测题

**Q1**：如何用 IO 流让 `"Hi"` 输出在宽度为 6 的字段中、**左对齐**、用 `*` 填充？
<details><summary>参考答案</summary><code>cout << setw(6) << setiosflags(ios::left) << setfill('*') << "Hi";</code> → 输出 <code>Hi****</code>。</details>

---

# 第 7 章 模板 ⭐⭐ 必考

## 7.1 核心概念

> **模板**：建立**通用模具**，提高复用性 → C++ 泛型编程的基础

特点：
- 模板**不能直接使用**，只是个框架
- 模板的**通用性不是万能的**（具体类型具体处理）

## 7.2 函数模板

### 语法

```cpp
template <typename T>  // 或 <class T>，typename 和 class 等价
void mySwap(T& a, T& b) {
    T temp = a; a = b; b = temp;
}
```

**必背关键词**：`template`、`typename`（或 `class`，两者等价）

### 两种使用方式

```cpp
mySwap(a, b);          // 1. 自动类型推导
mySwap<int>(a, b);     // 2. 显式指定类型
```

### ⚠️ 注意事项

1. **自动类型推导必须推出一致类型 T**：`mySwap(a, c)`（a int, c char）❌
2. 模板**必须能确定 T 才能使用**：`func()` ❌（无 T），`func<int>()` ✅

## 7.3 普通函数 vs 函数模板（重载调用规则）

| 情况 | 调用谁 |
|------|--------|
| 都能调 | **优先普通函数** |
| 想强制用模板 | 用**空模板参数列表** `mySwap<>(a, b)` |
| 只有模板匹配 | 调用模板 |
| 模板匹配度更高 | 调用模板 |

## 7.4 模板局限性 & 具体化

模板对自定义类型不友好（如 `Person` 之间不能直接 `==`）：

```cpp
template<typename T>
bool myCompare(T& a, T& b) { return a == b; }

// 针对 Person 的具体化模板（template<>）
template<> bool myCompare(Person& a, Person& b) {
    return a.name == b.name && a.age == b.age;
}
```

**有具体化模板优先调用具体化版本**。

## 7.5 类模板 ⭐⭐

### 语法

```cpp
template <typename NameType, typename AgeType>
class Person {
public:
    Person(NameType n, AgeType a) : name(n), age(a) {}
private:
    NameType name;
    AgeType  age;
};
Person<string, int> p("Tom", 18);  // ⚠️ 必须显式指定类型
```

### 与函数模板的区别

| 维度 | 函数模板 | 类模板 |
|------|---------|--------|
| 自动类型推导 | ✅ 可以 | **❌ 不行**（必须显式指定） |
| 默认参数 | ❌ | **✅ 可以** `template<class T, class U = int>` |

## 7.6 类模板成员函数创建时机

> **普通类**：成员函数一开始就创建
> **类模板**：成员函数**调用时才创建**（这就是为什么 .hpp 文件能解决分文件问题）

## 7.7 类模板做函数参数（三种方式）

```cpp
template<class T1, class T2>
class Person { /*...*/ };

// 方式1：指定传入类型
void func1(Person<string, int>& p);

// 方式2：参数模板化
template<class T1, class T2>
void func2(Person<T1, T2>& p);

// 方式3：整个类模板化
template<class T>
void func3(T& p);
```

## 7.8 类模板与继承

> ⚠️ **子类继承类模板时，必须指定父类中 T 的类型**

```cpp
template<class T>
class Base { T m; };

// 方式1：直接指定
class Son : public Base<int> {};

// 方式2：子类也变类模板
template<class T1, class T2>
class Son2 : public Base<T2> { T1 m; };
```

## 7.9 类模板分文件编写 ⚠️ 易错

> 类模板成员函数在调用时创建 → 分文件（.h + .cpp）会**链接失败**

**两种解决方案**：
1. 直接 `#include "person.cpp"`（不是 .h）
2. **将声明和实现写到同一个文件，后缀名改为 `.hpp`**（约定俗成）

## 7.10 类模板与友元

```cpp
// 全局函数类内实现：直接 friend
friend void print(Person<T1,T2> p) { /* 写在类内 */ }

// 全局函数类外实现：需要提前声明 + 空模板参数列表 <>
friend void print2<>(Person<T1,T2> p);
```

## 7.11 模板 极简示例

```cpp
// 函数模板
template<typename T>
T myMax(T a, T b) { return a > b ? a : b; }
cout << myMax(3, 5);       // 5
cout << myMax(3.1, 5.2);   // 5.2

// 类模板
template<class T>
class Box { T v; public: Box(T x):v(x){} T get(){return v;} };
Box<int> b(100);
```

## 7.12 模板 自测题

**Q1**：`template<typename T>` 中的 `typename` 可以换成什么？两者等价吗？
<details><summary>参考答案</summary>可以换成 <code>class</code>，两者**完全等价**，但更推荐用 <code>typename</code>（语义更清晰）。</details>

**Q2**：类模板对象做函数参数有哪三种方式？
<details><summary>参考答案</summary>① 指定传入类型 <code>Person&lt;string,int&gt;&amp;</code>；② 参数模板化 <code>Person&lt;T1,T2&gt;&amp;</code>；③ 整个类模板化 <code>T&amp;</code>。</details>

---

# 第 8 章 STL 初识

## 8.1 STL 六大组件 ⭐

1. **容器**（container）：各种数据结构（vector, list, map, set）
2. **算法**（algorithm）：常用算法（sort, find, count）
3. **迭代器**（iterator）：容器和算法之间的桥梁
4. **配接器/适配器**（adapter）：修饰容器/仿函数/迭代器
5. **仿函数**（function object）：行为类似函数
6. **空间配置器**（allocator）：负责空间管理

> **容器和算法之间通过迭代器进行无缝链接**

## 8.2 容器分类

| 类型 | 特点 | 代表 |
|------|------|------|
| **序列式容器** | 元素有固定顺序（位置） | vector, list, deque |
| **关联式容器** | 二叉树结构，按 key 组织 | set, multiset, map, multimap |

## 8.3 算法分类

| 类型 | 特点 | 例子 |
|------|------|------|
| **质变算法** | 运算中会修改元素内容 | 拷贝、替换、删除 |
| **非质变算法** | 不修改元素内容 | 查找、计数、遍历、极值 |

## 8.4 迭代器种类（必背表）⭐

| 种类 | 功能 | 支持运算 |
|------|------|---------|
| 输入迭代器 | 只读 | `++ == !=` |
| 输出迭代器 | 只写 | `++` |
| 前向迭代器 | 读写、向前 | `++ == !=` |
| 双向迭代器 | 读写、向前向后 | `++ --` |
| **随机访问迭代器** | 读写、跳跃访问 | `++ -- [n] -n < <= > >=` |

> **常用容器**：双向（list）+ 随机访问（vector）

## 8.5 vector 三种遍历方式 ⭐

```cpp
#include <vector>
#include <algorithm>
using namespace std;

vector<int> v = {1, 2, 3, 4};

// 方式1：迭代器
for (vector<int>::iterator it = v.begin(); it != v.end(); ++it)
    cout << *it;

// 方式2：for_each 算法
for_each(v.begin(), v.end(), [](int x){ cout << x; });

// 方式3：下标
for (int i = 0; i < v.size(); i++) cout << v[i];
```

**关键点**：
- `v.begin()` 指向**第一个元素**
- `v.end()` 指向**最后一个元素的下一个位置**

## 8.6 vector 极简示例

```cpp
vector<int> v;
v.push_back(10);
v.push_back(20);
v.push_back(30);
cout << v.size();  // 3
cout << v[0];      // 10
```

## 8.7 STL 自测题

**Q1**：STL 六大组件是哪六个？
<details><summary>参考答案</summary>容器、算法、迭代器、配接器（适配器）、仿函数、空间配置器。</details>

**Q2**：vector 迭代器 `v.begin()` 和 `v.end()` 分别指向什么？
<details><summary>参考答案</summary><code>v.begin()</code> 指向**第一个元素**；<code>v.end()</code> 指向**最后一个元素的下一个位置**（不存在的尾后位置）。</details>

---

# 📋 考试重点速查（必背）

> 这是你考试范围里**明确提到的 9 个高频点**，按重要度排序：

| # | 知识点 | 关键要点 |
|---|--------|---------|
| 1 | **静态成员对象** | 类内声明 + 类外初始化；静态函数只能访问静态成员 |
| 2 | **this 指针 + 运算符重载** | 返回 `*this` 支持链式；`this` 是 `T* const` |
| 3 | **拷贝构造函数** | 三种调用时机；浅拷贝陷阱 → 必须深拷贝 |
| 4 | **继承方式区别** | public/protected/private 继承下父类成员权限变化 |
| 5 | **多态** | 三个条件：继承 + virtual 重写 + 父类指针/引用 |
| 6 | **虚继承 / 虚基类** | `virtual public` 解决菱形继承二义性 + 数据冗余 |
| 7 | **运算符重载** | 重点：`+` / `<<`（必须友元+全局）/ `++`（int 占位）/ `=`（深拷贝） |
| 8 | **IO 流格式化** | `setw` + `ios::left` / `ios::right` + `setfill` |
| 9 | **模板** | 函数模板两参数等价；类模板无自动推导；分文件用 .hpp |

---

# 附录 A：自测题参考答案汇总

> 完整答案已嵌入各章节 `<details>` 块，下方汇总方便最后冲刺时一眼看完：

**第 1 章**
1. 不能。返回了局部变量的引用，函数结束后 a 被销毁，引用成为野引用。

**第 2 章**
1. 不能。仅返回值不同不能构成重载，调用时编译器无法区分。

**第 3 章**
1. 浅拷贝问题：p1 和 p2 的 age 指向同一块堆区，析构时重复 delete 崩溃。修复：自定义拷贝构造函数做深拷贝 `Person(const Person& p) { age = new int(*p.age); }`
2. 重载 `==` 运算符：`bool operator==(Person& p) { return name==p.name && age==p.age; }`

**第 4 章**
1. private
2. 不合法，二义性。方案①加作用域 `st.Sheep::m_A`；方案②用虚继承使数据只有一份。

**第 5 章**
1. 同一接口表现不同行为。条件：① 继承关系 ② 子类重写父类虚函数 ③ 父类指针或引用指向子类对象
2. 只调父类析构，子类堆区泄漏。解决：父类析构改为虚析构或纯虚析构。

**第 6 章**
1. `cout << setw(6) << setiosflags(ios::left) << setfill('*') << "Hi";` → `Hi****`

**第 7 章**
1. 可以换成 `class`，两者完全等价。
2. ① 指定传入类型；② 参数模板化；③ 整个类模板化。

**第 8 章**
1. 容器、算法、迭代器、配接器、仿函数、空间配置器。
2. `v.begin()` 指向第一个元素；`v.end()` 指向最后一个元素的下一个位置。

---

# 附录 B：考试前一天终极速记

1. **菱形继承** → `virtual public`
2. **多态** → virtual + 重写 + 父类指针/引用
3. **深拷贝** → 拷贝构造 + operator= + 析构（有指针时）
4. **左对齐输出** → `setw + ios::left + setfill`
5. **左移 <<** → 必须全局函数 + 友元 + 返回 `ostream&`
6. **后置 ++** → 加 `int` 占位 + 返回值（不是引用）
7. **类模板分文件** → 用 .hpp
8. **类模板对象做参数** → 必须显式指定类型
9. **抽象类** = 含纯虚函数 → 不能实例化
10. **虚析构** = 解决父类指针释放子类对象

> 🎯 **搞定这 10 条，C++ 期末稳过！**
