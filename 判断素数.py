num = int(input("请输入一个整数: "))
if num > 1:
   for i in range(2, int(num ** 0.5) + 1):
       if num % i == 0:
           print(f"{num}不是素数")
           break
   else:
       print(f"{num}是素数")
else:
   print(f"{num}不是素数")
