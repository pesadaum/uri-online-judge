product_1 = [int(input()) if i < 2 else float(input()) for i in range(3)]
product_2 = [int(input()) if i < 2 else float(input()) for i in range(3)]

value = product_1[1] * product_1[2] + product_2[1] * product_2[2]

print("VALOR A PAGAR: R$ {:.2f}".format(value))
