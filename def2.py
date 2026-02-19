# 检测输入的中文字符串是否符合回文的语法，
def backword():
    if s==s[::-1]:
        return f"[{}]是回文"
    else:
        return f"[{}]不是回文"
exam_word=str(input("输入一段字符串:"))
print(backword(exam_word))

# 模拟栈
# 取出命令（pop）、压栈命令（push）、
# 显示最后一个入栈的数字(top)、退出指令(exit)
word=[]
def push(a):
 word.append(a)
 print("栈:\n")
 for i in range(len(word)-1,-1,-1):
  print(f"{word[i]}")
def pop():
 print(f"{word[-1]}")
 word.pop(-1)
 print("栈:\n")
 for i in range(len(word)-1,-1,-1):
  print(f"{word[i]}\n")
def top():
  print(word[-1])
while True:
    line=input("请输入指令(push/pop/top/exit):")
    if line=="push":
        s=input("请输入要存入栈的数字:")
        push()
    elif line=="pop":
        pop()
    elif line=="top":
        top()
    elif line=="exit":
        break
    else:
        print("请正确输入指令!")
