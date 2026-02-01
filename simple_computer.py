#简易计算器
#功能要求：
#1. 支持加(+)、减(-)、乘(*)、除(/)四种运算
#2. 用户可以连续计算，直到选择退出
#3. 处理异常情况（如除数为零）
n1=float(input("请输入一个数字"))
ne=input("输入一个基础运算符号(‘+，-，*，/’)")
n2=float(input("请再输入一个数字"))
result=0
if ne=="+":
    result=n1+n2
elif ne=="-":
    result=n1-n2
elif ne=="*":
    result=n1*n2
elif ne=="/":
    if n2==0:
        print("除数不可为0！")
    else:
        result=n1/n2
else:
    print("请输入正确的算式")
print(n1,"+",n2,"=",result)    
