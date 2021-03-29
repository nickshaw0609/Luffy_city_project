import random
"""
输入格式：
3（组数）                                            
4（每组牌数）                                                 
0 1 1 1         每组抽一张牌，使连续的1最多，输出每组结果          3
5（每组牌数）     --------------------------------->   
0 1 0 1 1                                                   3
2（每组牌数）
1 1                                                         1
"""


def generate_data(groups, *num):
    """
    生成数据
    :param groups: 数据组数
    :param num: 各组数据数量
    :return list_res: 返回数据列表
    """
    list_res = []
    if len(num) != groups:
        print("输入组类别数量不等于总组数，请重新输入")
    else:
        print(groups)
        for i in num:
            list_n = []
            for each in range(i):
                list_n.append(random.randint(0, 1))
            list_res.append([i, list_n])
        return list_res


def judge(list_res):
    """
    判断抽排
    :param list_res:
    :return: 返回抽排结果列表[1,2,4,2,...]
    """
    for each in list_res:
        li = [str(i) for i in each[1]]
        val_str = "".join(li)
        print(val_str)
        print(val_str.count("101"))





list_res = generate_data(5, 8, 8, 7, 7, 9)
print(list_res)
judge(list_res)