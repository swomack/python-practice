
s = "hello"
count = [10,20,30,40,50,60]
dic = dict()
dic['a'] = 1
dic['b'] = 2

print(dic.values())

for pair in zip(s, count, dic, dic.values()):
    print(pair)

t = list(zip(s, count, dic, dic.values()))
print(t)


dic = {'a' : 100, 'b' : 200}

tu = dic.items()

for k, v in tu:
    print(k ,v)




