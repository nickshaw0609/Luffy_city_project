f = open("flies/txt1.txt", "r+", encoding="utf-8")
i = 5
while i:
    f.write("倪锦潇")
    i -= 1
print(f.seek(3))
line = f.read()
print(line)
f.close()

f1 = open("flies/1.png", "rb")
pic1 = f1.read()
f1.close()

f2 = open("flies/1_dup.png", "wb")
f2.write(pic1)
f2.close()
