#请按照要求编写一个网站的注册模块
#用户名不允许重复
#数据库需要保存用户名及密码
#初始用户及密码（"小甲鱼":"I_love_FishC"，"不二如是":"FishC5201314"）
import hashlib  
#安全加密为附加内容
x=dict({"小甲鱼":"I_love_FishC","不二如是":"FishC5201314"})
while True:
    thename = input("请输入用户名:")
    if thename in x:
        print("该用户名已被注册！")
    else:
        break
passnumber=input("请输入密码:")
x[thename]=passnumber
print("----------------------\n目前已注册的用户有:")
for i in x:
    result = hashlib.md5(b"{i}")
    print(f"{i}:{result.hexdigest()}")
