input_value = int(input())
count = 0


def sol(n):
    global count
    if n < 100:
        count = count + 1
    else:
        number_left = int(str(n)[0])
        number_mid = int(str(n)[1])
        number_right = int(str(n)[2])
        if (number_right - number_mid) == (number_mid - number_left):
            count = count + 1


for i in range(1, input_value + 1):
    sol(i)

print(count)
