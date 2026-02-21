# 罗马数字包含 I、V、X、L、C、D、M 七种字符，分别表示数值 1、5、10、50、100、500、1000。
# 将数字 2 写做罗马字符的形式是 II（即 I + I），数字 12 写做 XII（即 X + I + I），27 写做 XXVII
# 即 X + X + V + I + I。
# 如:一颗大白菜 27 元，那么就给两张10元，一张5元和两张1元这样的组合。
# 罗马字符的组合也存在一些特殊规则，比如 4 不写做 IIII，
# 而是 IV（即 I 在 V 的左边，表示 5 - 1，因此得到数字 4）。
# I 可以放在 V（5）和 X（10）的左边，表示 4 和 9
# X 可以放在 L（50）和 C（100）的左边，表示 40 和 90
# C 可以放在 D（500）和 M（1000）的左边，表示 400 和 900)
def transform(roma):
    # 罗马数字映射表
    roma_excel = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    prev_value = 0
    # 从右向左遍历（处理减法规则更方便）
    for char in reversed(roma):
        current_value = roma_excel[char]
        # 如果当前值小于前一个值，说明是减法情况（如 IV）
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        prev_value = current_value
    return total
# 主程序
roma = input("请输入一段罗马数字: ").upper()  # 转换为大写
roma_check = ("I", "V", "X", "L", "C", "D", "M")
# 检查每个字符是否合法
valid = True
for char in roma:
    if char not in roma_check:
        print(f"错误: '{char}' 不是有效的罗马数字字符!")
        valid = False
        break
if valid and roma:  # 确保输入不为空
    result = transform(roma)
    print(f"罗马数字 {roma} 对应的阿拉伯数字是: {result}")
else:
    print("请输入有效的罗马数字!")
