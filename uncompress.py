#解压缩
s = str(input())
result = ""
i = 0
while i < len():
    char = s[i]
    i += 1
    # 如果下一个字符是数字
    if i < len() and[i].isdigit():
        num = ""
        while i < len() and[i].isdigit():
            num += s[i]
            i += 1
        # 解压：字符重复num次
        result += char * int(num)
    else:
        # 没有数字，直接添加字符
        result += char
print(result)
