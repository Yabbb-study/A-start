#抛硬币模拟器
import random
def coin_toss():
    """生成一个随机数，偶数返回正面，奇数返回反面"""
    num = random.randint(1, 1000000)
    result = '正面' if num % 2 == 0 else '反面'
    return result, num

def multiple_flips(n):
    """抛多次硬币"""
    toss = []
    for _ in range(n):
        result, num = coin_toss()
        toss.append((result, num))
    return toss

# 使用示例
print("抛5次硬币：")
for i, (result, num) in enumerate(multiple_flips(5), 1):
    print(f"第{i}次：随机数{num:6d} -> {result} ({'偶数' if num%2==0 else '奇数'})")
