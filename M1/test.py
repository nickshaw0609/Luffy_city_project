# students=[
#     {'name':'tom','age':18,'hobbies':['sing','play']},
#     {'name':'rose','age':88,'hobbies':['read','sleep']},
#     {'name':'jack','age':99,'hobbies':['swim','watchTV','talk']},
# ]
#
# print(students[2]["hobbies"][1])
#
# name='tom say hello world,tom say bye'
# name2=name.replace("tom", "rose", 1)
# print()
#
# count=0
# for i in range(2, 101,2):
#     print(i)
#     count += i
# print(count)
#
# info={
# 'egon':{'pwd':'123','hobbies':['play','music','read']},
# 'alex':{'pwd':'1234','hobbies':['music','read']},
# 'wupeiqi':{'pwd':'135','hobbies':['read',]},
# }
#
#
# print(id(info))
# print(id(info['alex']['hobbies']))
# info['alex']['hobbies'].append('play')  # 给alex追加play的爱好
#
# print(info)
# print(id(info))
# print(id(info['alex']['hobbies']))
#
# li=[1,2,3]
# li2=[1,2,3]
# print(id(li))
# print(id(li2))
#
#
# year = input("请输入年份：")
# if year.isdigit():
#     year = int(year)
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
#         print("该年份是闰年！")
#     else:
#         print("该年份不是闰年！")

# li = ['周','麻花藤','周扒皮']
# for i in li:
#     if i.startswith("周"):
#         li.remove(i)
# print(li)

li = ['周', '周星星', '麻花藤', '周扒皮']
print(list(filter(lambda x: x[0] != '周', li)))

#
dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
dic.pop("k1")
print(dic)


# 方式1：

# for i in range(len(li)-1,-1,-1):
#     print(i)
#     print(li[i])
#     if li[i][0] =='周':
#         li.pop(i)
# print(li)

li = ['alex', 'eric', 'rain']
for i,v in enumerate(li,100):
    print(i,v)
print(dict(enumerate(li, 1)))

a,b=[1,2]
print(a,b)
