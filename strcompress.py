# 利用字符重复出现的次数，编写一个程序，实现基本的字符串压缩功能。
# 比如，字符串 FFiiiisshCCCCCC 压缩后变成 F2i4s2h1C6（15字符 -> 10字符，66% 压缩率）
# 输入字符串
# 初始化
s=str(input())
result = ""
count = 1
current = s[0]
# 遍历字符串
for i in range(1, len()):
    if[i] == current:
        count += 1
    else:
        # 处理前一个字符
        if count > 2:
            result = result + current + str(count)
        else:
            result = result + current * count

        # 重置
        current = s[i]
        count = 1

# 处理最后一个字符
if count > 2:
    result = result + current + str(count)
else:
    result = result + current * count

# 压缩率
original_len = len()
compressed_len = len(result)
compression_rate = (1 - compressed_len / original_len) * 100

print("原始字符串:", s)
print("压缩后:", result)
print(f"压缩率: {compression_rate:.1f}%")



