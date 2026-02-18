# 编写 2个函数分别用于注册（register()）、登陆（login())
# 使用一个 Python 的字典作为数据库。
# 注册时需验证用户名是否已存在于数据库
# 登陆时需验证用户名和密码是否匹配
name={}
def register():
    username = input("请输入用户名:")
    if username in name:
        print("用户名已存在！")
        return
    password = input("请输入密码:")
    name[username] = password
    print("恭喜！注册成功！")
def login():
    logname = input("请输入用户名:")
    if logname not in name:
        print("未找到该用户名。")
        return
    passlog=input("请输入密码:")
    if name[logname]==passlog:
        print("登录成功!")
        return
while True:
     print("1.注册\n2.登录\n3.退出")
     sel=int(input("请输入指令:"))
     if sel==3:
          print("感谢使用！")
          break
     elif sel==1:
          register()
     elif sel==2:
          login()
     else:
          print("请输入有效指令。")
