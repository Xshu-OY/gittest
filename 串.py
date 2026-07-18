#串的操作


class String(object):
    def __init__(self):
        self.MaxStringSize=256
        self.chars=""
        self.length=0
    def IsEmpty(self):            # 判断是否为空
        if self.length ==0:
            IsEmpty=True
        else:
            IsEmpty=False
        return IsEmpty
    def CreateString(self):                       # 创建串
        stringSH= input("请输入字符串：")
        if len(stringSH) > self.MaxStringSize:
            print("溢出，超过的部分无法保存")
            self.chars=stringSH[:self.MaxStringSize]
        else:
            self.chars=stringSH
    def StringConcat(self,strSrc):                 # 串连接
        lengthSrc = len(strSrc)
        stringSrc = strSrc
        if lengthSrc + len(self.chars) <= self.MaxStringSize:
            self.chars=self.chars+stringSrc
        else:
            print("两个字符的长度之和溢出，超过的部分无法显示")
            size=self.MaxStringSize-len(self.chars)
            self.chars=self.chars+stringSrc[:size]
        print("连接后字符串为：",self.chars)
    def SubString(self,iPos,length):      # 从iPos位置开始，取长度为length的子串
        if iPos>len(self.chars)-1 or iPos<0 or length<1 or (length+iPos)>len(self.chars):
            print("无法获取")
        else:
            substr = self.chars[iPos:iPos+length]
            print("获取的字串为：",substr)

if __name__ == "__main__":
    string = String()
    print(string.IsEmpty())
    string.CreateString()
    string.StringConcat("123")
    string.SubString(1,4)




# BF算法
def BF(s1,s2,pos = 0):   # BF算法
    i = pos
    j = 0
    while(i < len(s1) and j < len(s2)):
        if(s1[i] ==  s2[j]):
            i += 1
            j += 1
        else:
            i = i - j + 1           #目标串S 的i 回滚
            j = 0                #模式串T
    if(j >= len(s2)):
        return i - len(s2)
    else:
        return 0
if __name__ == "__main__":
    s1 = "BBC ABCDAB ABCDABCDABDE"
    s2 = "ABCDABD"
print(BF(s1,s2))



# KMP算法

#coding=utf-8
def kmp_match(s, p):     #KMP 算法
    m = len(s);
    n = len(p)
    cur = 0  # 起始指针cur
    table = partial_table(p)
    while cur <= m - n:     #只去匹配前m-n个
        for i in range(n):
            if s[i + cur] != p[i]:
                cur += max(i - table[i - 1], 1)  # 有了部分匹配表,可以一次移动多位
                break
        else:      #如果没有从任何一个 break 中退出，则会执行和 for 对应的 else
                        #只要从 break 中退出了，则 else 部分不执行。
            return True
    return False

# 部分匹配表
def partial_table(p):
    '''''partial_table("ABCDABD") -> [0, 0, 0, 0, 1, 2, 0]'''
    prefix = set()
    postfix = set()
    ret = [0]
    for i in range(1, len(p)):
        prefix.add(p[:i])
        postfix = {p[j:i + 1] for j in range(1, i + 1)}
        ret.append(len((prefix & postfix or {''}).pop()))
    return ret
print(partial_table("ABCDABD"))
print(kmp_match("BBC ABCDAB ABCDABCDABDE", "ABCDABD"))
