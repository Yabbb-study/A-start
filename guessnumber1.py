import random
answer = random.randint(1,55)
count=3
while count>0:
    a = input("从1-55里猜一个数字吧！！")
    guess=int(a)
    if guess==answer:
         print("你也太厉害了吧！！")
         break
    else:
        if guess>answer:
          print("有些太大了哦！")
        else:
          print ("有些太小了owo")
    count-=1
