f = open("flies/sign_up_data.txt", "a+", encoding="utf-8")
while True:
    ID = input("请输入注册名：").replace(" ", "")
    if ID.upper() == "Q":
        break
    f.seek(0)
    if ID not in f.read():
        psw = input("请输入密码：").replace(" ", "")
        psw_check = input("请确认密码：").replace(" ", "")
        if psw == psw_check:
            print(f"注册成功!用户名为：{ID}")
            f.write(f"用户名：{ID}   密码：{psw}\n")
        else:
            print("两次密码输入错误！")
    else:
        print("用户名已存在！")
        continue

f.close()
