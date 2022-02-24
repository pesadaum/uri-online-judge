from math import sqrt

inputs = input().split(" ")

a, b, c = [float(i) for i in inputs]


def calculate_roots_baskara(a, b, c):

    delta = ((b**2) - (4*a*c))

    if delta < 0 or a == 0:
        print("Impossivel calcular")
    else:
        x1 = (-b + sqrt(delta)) / (2*a)
        x2 = (-b - sqrt(delta)) / (2*a)

        print(f"R1 = {x1:.5f}\nR2 = {x2:.5f}")


calculate_roots_baskara(a, b, c)
