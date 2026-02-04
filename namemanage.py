print("按1录入名字\n按2查询\n按3删除名字\n按0结束程序")
name=[]                                                 #一个管理个人信息的小程序  还没写完！之后会尝试另外再写一个成绩管理功能
while True:
    a = int(input("请选择一个功能："))
    if a==1:
        b=(input("请输入一个名字："))
        print(b)
        name.append(b)
    elif a==2:
        print(f"已录入名字:\n{name}")
    elif a==3:
        print(f"当前已录入的名字{name}")
        print("选择你要删除的名字:")
        c=(input())
        name.remove(c)
    elif a==0:
        print("程序已退出！感谢使用！！")
        break
    else:
        print("输入的数字无效！")
