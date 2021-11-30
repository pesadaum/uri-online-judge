inputs = input().split(" ")

input_int = [int(i) for i in inputs]


def bigger_ab(a, b):
    return (a+b + abs(a-b))//2


bigger_temp = bigger_ab(input_int[0], input_int[1])
bigger = bigger_ab(bigger_temp, input_int[2])

print("{} eh o maior".format(bigger))
