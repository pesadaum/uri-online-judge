inputs_1 = input().split(" ")
input_float_1 = [float(i) for i in inputs_1]

inputs_2 = input().split(" ")
input_float_2 = [float(i) for i in inputs_2]

x1, y1 = input_float_1
x2, y2 = input_float_2

distance = (((x2-x1)**2) + ((y2 - y1)**2))**(1/2)

print("{:.4f}".format(distance))
