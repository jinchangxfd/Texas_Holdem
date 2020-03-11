from functools import cmp_to_key


# 判断大小 计算差值
def cmp(a, b):
    lt_list = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    return lt_list.index(a[0]) - lt_list.index(b[0])


# 判断牌型
def poker_hand(hand_list=[]):
    re_list = sorted(hand_list, key=cmp_to_key(cmp))

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
    if lt_list.index(a[0]) < lt_list.index(b[0]):
        return -1

    # 散牌
    if a[0] == 'High Card':
        if cmp(a[1], b[1]) > 0:
            return 1
        elif cmp(a[1], b[1]) < 0:
            return -1
        else:
            if cmp(a[2], b[2]) > 0:
                return 1
            elif cmp(a[2], b[2]) < 0:
                return -1
            else:
                if cmp(a[3], b[3]) > 0:
                    return 1
                elif cmp(a[3], b[3]) < 0:
                    return -1
                else:
                    if cmp(a[4], b[4]) > 0:
                        return 1
                    elif cmp(a[4], b[4]) < 0:
                        return -1
                    else:
                        if cmp(a[5], b[5]) > 0:
                            return 1
                        elif cmp(a[5], b[5]) < 0:
                            return -1
                        else:
                            return 0

    # 对子
    if a[0] == 'Pair':
        if cmp(a[1], b[1]) > 0:
            return 1
        elif cmp(a[1], b[1]) < 0:
            return -1
        else:
            if cmp(a[2], b[2]) > 0:
                return 1
            elif cmp(a[2], b[2]) < 0:
                return -1
            else:
                if cmp(a[3], b[3]) > 0:
                    return 1
                elif cmp(a[3], b[3]) < 0:
                    return -1
                else:
                    if cmp(a[4], b[4]) > 0:
                        return 1
                    elif cmp(a[4], b[4]) < 0:
                        return -1
                    else:
                        return 0

    # 两对
    if a[0] == 'Two Pairs':
        if cmp(a[1], b[1]) > 0:
            return 1
        elif cmp(a[1], b[1]) < 0:
            return -1
        else:
            if cmp(a[2], b[2]) > 0:
                return 1
            elif cmp(a[2], b[2]) < 0:
                return -1
            else:
                if cmp(a[3], b[3]) > 0:
                    return 1
                elif cmp(a[3], b[3]) < 0:
                    return -1
                else:
                    return 0

    # 三条
    if a[0] == 'Three of a Kind':
        if cmp(a[1], b[1]) > 0:
            return 1
        elif cmp(a[1], b[1]) < 0:
            return -1
        else:
            return 0

    # 顺子
    if a[0] == 'Straight':
        if cmp(a[1], b[1]) > 0:
            return 1
        elif cmp(a[1], b[1]) < 0:
            return -1
        else:
            return 0

    # 同花
    if a[0] == 'Flush':
        if cmp(a[1], b[1]) > 0:
            return 1
        elif cmp(a[1], b[1]) < 0:
            return -1
        else:
            if cmp(a[2], b[2]) > 0:
                return 1
            elif cmp(a[2], b[2]) < 0:
                return -1
            else:
                if cmp(a[3], b[3]) > 0:
                    return 1
                elif cmp(a[3], b[3]) < 0:
                    return -1
                else:
                    if cmp(a[4], b[4]) > 0:
                        return 1
                    elif cmp(a[4], b[4]) < 0:
                        return -1
                    else:
                        if cmp(a[5], b[5]) > 0:
                            return 1
                        elif cmp(a[5], b[5]) < 0:
                            return -1
                        else:
                            return 0

    # 葫芦
    if a[0] == 'Full House':
        if cmp(a[1], b[1]) > 0:
            return 1
        elif cmp(a[1], b[1]) < 0:
            return -1
        else:
            return 0

    # 铁支
    if a[0] == 'Four of a kind':
        if cmp(a[1], b[1]) > 0:
            return 1
        elif cmp(a[1], b[1]) < 0:
            return -1
        else:
            return 0

    # 同花顺
    if a[0] == 'Straight flush':
        if cmp(a[1], b[1]) > 0:
            return 1
        elif cmp(a[1], b[1]) < 0:
            return -1
        else:
            return 0


# 判断胜负
def who_win(input_str):
    # 数据规范化
    input_list = input_str.split(' ')
    name1 = input_list[0][:-1]
    hand1 = []
    hand2 = []
    for i in range(1, 6):
        hand1.append(list(input_list[i]))
    poker_hand(hand1)
    name2 = input_list[6][:-1]
    for i in range(7, 12):
        hand2.append(list(input_list[i]))

    hand1 = poker_hand(hand1)
    hand2 = poker_hand(hand2)

    x = cmp_poker(hand1, hand2)
    if x == 1:
        print(name1 + ' wins')
        return name1 + ' wins'
    elif x == -1:
        print(name2 + ' wins')
        return name2 + ' wins'
    else:
        print('Tie')
        return 'Tie'


if __name__ == '__main__':
    who_win('Black: AH KD 7S 4H 7C White: 2C 3H 4S 8C AH')
    who_win('Black: 2H 3D 5S 9C KD B: 2C 3H 4S 8C AH')
