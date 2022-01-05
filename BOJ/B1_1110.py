first_data = int(input())
count = 0


def add_cycle(number):
    global count

    count = count + 1
    number_left = 0
    if number >= 10:
        number_left = number // 10
    number_right = number % 10
    new = (number_left + number_right) % 10
    ans = number_right * 10 + new
    if ans == first_data:
        return
    add_cycle(ans)


add_cycle(first_data)
print(count)
