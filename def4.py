模拟斗地主,注意：本次代码大量参考AI
import random
def fy_shuffle(data, shuffle_times=1):
    """
    Fisher-Yates 原始版洗牌（取出放到新列表）
    :param data: 可迭代对象
    :param shuffle_times: 洗牌次数
    :return: 打乱后的列表
    """
    current_list = list(data)  # 复制一份，不改变原数据
    for _ in range(shuffle_times):
        source = current_list[:]  # 当前要打乱的列表
        result = []
        while source:
            k = random.randint(1, len(source))  # 1 到剩下数字个数
            # 第 k 个（索引 k-1）
            item = source.pop(k - 1)
            result.append(item)
        current_list = result  # 作为下一次洗牌的源
    return current_list


def build_deck():
    """生成一副牌"""
    suits = ['黑桃', '红心', '梅花', '方块']
    numbers = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']
    deck = [s + n forin suits for n in numbers]
    deck.append('joker')  # 小王
    deck.append('JOKER')  # 大王
    return deck


def deal_landlord(deck):
    """
    斗地主发牌
    :param deck: 一副牌列表
    :return: (玩家1牌, 玩家2牌, 玩家3牌, 地主牌, 地主索引)
    """
    shuffled = fy_shuffle(deck, shuffle_times=1)
    player1 = shuffled[:17]
    player2 = shuffled[17:34]
    player3 = shuffled[34:51]
    landlord_cards = shuffled[51:]  # 最后 3 张

    landlord_index = random.randint(0, 2)  # 0:玩家1, 1:玩家2, 2:玩家3
    if landlord_index == 0:
        player1.extend(landlord_cards)
    elif landlord_index == 1:
        player2.extend(landlord_cards)
    else:
        player3.extend(landlord_cards)

    return player1, player2, player3, landlord_cards, landlord_index

if __name__ == '__main__':
    deck = build_deck()
    print(f"原始牌堆 ({len(deck)}张): {deck}\n")

    p1, p2, p3, landlord_cards, landlord = deal_landlord(deck)
    print(f"地主是玩家{landlord + 1}，地主牌: {landlord_cards}")
    print(f"玩家1 ({len(p1)}张): {sorted(p1)}")  # 排序一下好看
    print(f"玩家2 ({len(p2)}张): {sorted(p2)}")
    print(f"玩家3 ({len(p3)}张): {sorted(p3)}")
