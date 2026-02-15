#生成一个随机数列表，一共有 100 个元素，每个元素取 1~100 的随机值，赋值给变量 x
#生成另一个随机数列表，一共有 100 个元素，每个元素取 50~150 的随机值，赋值给变量 y
#利用字典的 “键” 不会重复的特点，计算 x 和 y 的交集（就是两者共有的元素）
import  random
a=0
d=[]
e=[]
x=dict()
y=dict()
while a!=100:
    b=random.randint(1,100)
    c=random.randint(50,150)
    a+=1
    d.append(b)
    e.append(c)
x=dict.fromkeys(d)
y=dict.fromkeys(e)
inter=x.keys()&y.keys()
print(inter)

# 生成 0~999999 所有整数组成密码的哈希值
# 将上面生成的哈希值保存为映射类型
# 通过查表的方式，计算下面 3 个哈希值对应的明文密码
import hashlib
hasher = {}
for x in range(0, 1000000):
    hashnumber = hashlib.md5(str(x).encode()).hexdigest()
    hasher[x] = hashnumber
  #题目来源小甲鱼
