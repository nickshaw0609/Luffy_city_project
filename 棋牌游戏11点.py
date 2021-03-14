import random


def generate():
    """
    生成一副扑克牌,并赋值
    :return: poker_list[['♥A', 1], ['♦A', 1], ['♣A', 1], ['♠A', 1],.... ]
    """
    poker_list = []  # 扑克牌列表
    variety = ["♥", "♦", "♣", "♠"]  # 花色列表
    poker_type = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 赋值即为牌名
    special_type1 = ["J", "Q", "K"]  # JQK赋值为0.5
    special_type2 = [["Joker_vice", 0.5], ["Joker", 0.5]]  # 大王小王赋值为0.5

    for num in poker_type:
        for each in variety:
            poker_list.append([f"{each}{num}", poker_type.index(num) + 1])  # 生成A~10列表：[[扑克牌, 赋值], ...]

    for num in special_type1:
        for each in variety:
            poker_list.append([f"{each}{num}", 0.5])  # 生成J,Q,K列表：[[扑克牌, 赋值], ...]

    poker_list.extend(special_type2)  # 添加大小王
    return poker_list


def calc(player_cards_dic):
    """
    计算当前手牌值之和，大于11则清零
    :param player_cards_dic: 需要计算得分的玩家字典{'alex': [['♦A', 1], ['♦8', 8]],....}
    :return:result{"alex":8,"武沛齐":9,"李路飞":0}
    """
    result = {}  # 存储最终各位玩家的得分
    for players, cards in player_cards_dic.items():
        score = 0
        for index, i in enumerate(cards):
            p_num = i[1]
            score += p_num  # 统计该玩家所有手牌之和
            if score > 11:
                score = 0
        result[players] = score
    return result


def deliver(player_cards_dic, result, poker_list):
    """
    发牌器,如果玩家分数非零，则询问是否要牌
    :param player_cards_dic: 玩家当前手牌{}
    :param result: 玩家当前得分{}
    :param poker_list: 当前扑克牌组[]
    :return:当轮发牌后玩家手牌{}, 剩余扑克牌组[]
    """
    for players, score in result.items():
        while score != 0:
            answer = input(f"玩家{players},是否继续要牌?（Y/N）").strip(" ").upper()
            if answer not in ["Y", "N"]:
                answer = input("输入错误！请重新输入！").strip(" ").upper()
            if answer == "Y":
                res = random.sample(poker_list, 1)
                poker_list.remove(res[0])
                player_cards_dic[players].extend(res)  # 手牌加一
                score = calc(player_cards_dic)[players]  # 要牌后玩家的得分
                print(f"当前玩家{players}手牌:{player_cards_dic[players]},得分为{score}")
                if score == 0:
                    print(f"玩家{players}爆了！下一个玩家继续！")
                    break
                else:
                    continue
            else:
                break  # 输错一次重新输，再错直接跳过
    return player_cards_dic, poker_list


user_list = ["alex", "武沛齐", "李路飞"]
poker_list = generate()
player_cards_dic = {}  # 玩家手牌字典

# 首次发牌
for players in user_list:
    res = random.sample(poker_list, 1)
    poker_list.remove(res[0])
    player_cards_dic[players] = res
result = calc(player_cards_dic)  # 初次发牌结果得分
print("第一轮".center(50, "-"))
print("第一轮发牌结果：", player_cards_dic)  # 初次发牌结果
print("第一轮得分为：", result)
print("还剩{}张牌".format(len(poker_list)))

# 第二轮发牌
print("第二轮".center(50, "-"))
player_cards_dic, poker_list = deliver(player_cards_dic, result, poker_list)  # 第二次发牌结果
result = calc(player_cards_dic)  # 第二次得分
print("第二轮发牌结果：", player_cards_dic)
print("第二轮得分为：", result)
print("还剩{}张牌".format(len(poker_list)))

# TODO 接下来可以再定义函数 "def deliver_N():",解决N次发牌的问题：流程为首次发牌>>计算得分>>....>>第N次发牌>>计算第N次得分>>....>>得出胜者
