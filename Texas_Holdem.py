# 判断牌型
def poker_hand(l=[]):
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
    name2 = input_list[6][:-1]
    for i in range(7, 12):
        hand2.append(list(input_list[i]))
    print(hand2)


if __name__ == '__main__':
    who_win('Black: 6H 7D 7S 7H 7C White: 2C 3H 4S 8C AH')
