product_1 = []
product_2 = []

for i in range(3):
    product_1.append(float(input()))

for i in range(3):
    product_2.append(float(input()))


value = product_1[1] * product_1[2] + product_2[1] * product_2[2]

print("VALOR A PAGAR: R$ {:.2f}".format(value))
