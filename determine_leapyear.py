# 题目：判断闰年
# 目标：输入一个年份，判断它是不是闰年

year = input("请输入年份：")
year = int(year)
if year % 400 == 0:
    print(f"{year}是闰年")
elif year % 4 == 0 and year % 100 != 0:
    print(f"{year}是闰年")
else:
    print(f"{year}不是闰年")
