from functools import cmp_to_key


# 判断大小 计算差值
def cmp(a, b):
    lt_list = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    return lt_list.index(a[0]) - lt_list.index(b[0])


# 判断牌型
def poker_hand(hand_list=[]):
    re_list = sorted(hand_list, key=cmp_to_key(cmp))
    print(re_list)

    # 同花顺
    if re_list[0][1] == re_list[1][1] == re_list[2][1] == re_list[3][1] == re_list[4][1] \
            and cmp(re_list[0], re_list[1]) == cmp(re_list[1], re_list[2]) == cmp(re_list[2], re_list[3]) == cmp(
                re_list[3], re_list[4]) == -1:
        return ['Straight flush', re_list[4][0]]

    # 铁支
    if re_list[0][0] == re_list[1][0] == re_list[2][0] == re_list[3][0]:
        return ['Four of a kind', re_list[0][0]]
    if re_list[4][0] == re_list[1][0] == re_list[2][0] == re_list[3][0]:
        return ['Four of a kind', re_list[4][0]]

    # 葫芦
    if re_list[0][0] == re_list[1][0] == re_list[2][0] and re_list[3][0] == re_list[4][0]:
        return ['Full House', re_list[0][0]]
    if re_list[0][0] == re_list[1][0] and re_list[3][0] == re_list[4][0] == re_list[2][0]:
        return ['Full House', re_list[4][0]]

    # 同花
    if re_list[0][1] == re_list[1][1] == re_list[2][1] == re_list[3][1] == re_list[4][1]:
        return ['Flush', re_list[4][0], re_list[3][0], re_list[2][0], re_list[1][0], re_list[0][0]]

    # 顺子
    if cmp(re_list[0], re_list[1]) == cmp(re_list[1], re_list[2]) == cmp(re_list[2], re_list[3]) == cmp(
            re_list[3], re_list[4]) == -1:
        return ['Straight', re_list[4][0]]

    # 三条
    if re_list[0][0] == re_list[1][0] == re_list[2][0]:
        return ['Three of a Kind', re_list[0][0]]
    if re_list[3][0] == re_list[1][0] == re_list[2][0]:
        return ['Three of a Kind', re_list[3][0]]
    if re_list[4][0] == re_list[3][0] == re_list[2][0]:
        return ['Three of a Kind', re_list[4][0]]

    # 两对
    if re_list[0][0] == re_list[1][0] and re_list[2][0] == re_list[3][0]:
        return ['Two Pairs', re_list[2][0], re_list[0][0], re_list[4][0]]
    if re_list[0][0] == re_list[1][0] and re_list[4][0] == re_list[3][0]:
        return ['Two Pairs', re_list[4][0], re_list[0][0], re_list[2][0]]
    if re_list[2][0] == re_list[1][0] and re_list[4][0] == re_list[3][0]:
        return ['Two Pairs', re_list[4][0], re_list[2][0], re_list[0][0]]

    # 对子
    if re_list[0][0] == re_list[1][0]:
        return ['Pair', re_list[0][0], re_list[4][0], re_list[3][0], re_list[2][0]]
    if re_list[2][0] == re_list[1][0]:
        return ['Pair', re_list[2][0], re_list[4][0], re_list[3][0], re_list[0][0]]
    if re_list[2][0] == re_list[3][0]:
        return ['Pair', re_list[2][0], re_list[4][0], re_list[1][0], re_list[0][0]]
    if re_list[3][0] == re_list[4][0]:
        return ['Pair', re_list[3][0], re_list[2][0], re_list[1][0], re_list[0][0]]

    # 散牌
    return ['High Card', re_list[4][0], re_list[3][0], re_list[2][0], re_list[1][0], re_list[0][0]]


# 按牌型比大小
def cmp_poker(a, b):
    lt_list = ['High Card', 'Pair', 'Two Pairs', 'Three of a Kind', 'Straight', 'Flush', 'Full House',
               'Four of a kind', 'Straight flush']
    if lt_list.index(a[0]) > lt_list.index(b[0]):
        return 1
    if lt_list.index(a[0]) > lt_list.index(b[0]):
        return 0


# 判断胜负
def who_win(input_str):
    # 数据规范化
    input_list = input_str.split(' ')
    print(input_list)
    name1 = input_list[0][:-1]
    hand1 = []
    hand2 = []
    for i in range(1, 6):
        hand1.append(list(input_list[i]))
    print(hand1)
    poker_hand(hand1)
    name2 = input_list[6][:-1]
    for i in range(7, 12):
        hand2.append(list(input_list[i]))
    print(hand2)


if __name__ == '__main__':
    who_win('Black: AH KD 7S 4H 7C White: 2C 3H 4S 8C AH')
