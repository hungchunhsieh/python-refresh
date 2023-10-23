
# s = "123ABC!!!"
s = "ABA!!!"

s = s.lower()

tem = ""

for i in s:
    # print(i)
    if i.isalpha():
        tem += i

if tem == tem[::-1]:
    print(True)
else:
    print(False)