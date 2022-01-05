ans_arr = [0 for i in range(10)]

first_input = int(input())
second_input = int(input())
third_input = int(input())

sum_value = first_input * second_input * third_input
sum_value = str(sum_value)
sum_len = len(sum_value)

for i in range(sum_len):
    ans_arr[int(sum_value[i])] = ans_arr[int(sum_value[i])] + 1

for i in range(10):
    print(ans_arr[i])
