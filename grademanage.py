print("按1录入成绩;按2查询成绩;按0退出程序")     #等把基础的过一遍再看看怎么把功能组合到一起owo
grade=[]
name=[]
while True:
    a=int(input("请选择功能："))
    if a==0:
        print("感谢您的使用！")
        break
    elif a==1:
        b=input("请输入姓名：")
        c=input("请输入该生的语数英成绩：")
        name.append(b)
        grade.append(c)
    elif a==2:
        print(name)
        d=input("请选择要查询的学生的姓名：")
        print(grade[name.index(d)])
