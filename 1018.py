value = int(input())

notes = [100, 50, 20, 10, 5, 2, 1]

for i in notes:
    curr_value = value // i
    value -= curr_value * i
    print("{} nota(s) de R$ {},00".format(curr_value, i))
