ans = [0 for i in range(1, 20000)]


def d(n):
    global ans
    str_input = str(n)
    len_input = len(str_input)
    new = 0
    for i in range(len_input):
        tmp = int(str_input[i])
        new = new + tmp
    ans[n+new] = 1


for i in range(10000):
    d(i)

for i in range(10000):
    if ans[i] == 0:
        print(str(i))
