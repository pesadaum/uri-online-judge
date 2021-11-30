inputs = input().split(" ")

input_float = [float(i) for i in inputs]

a, b, c = input_float


triangle = (a * c) / 2.0
circle = 3.14159 * c**2
trapezium = ((a + b) * c) / 2.0
square = b**2
rectangle = a * b

print("TRIANGULO: {:.3f}".format(triangle))
print("CIRCULO: {:.3f}".format(circle))
print("TRAPEZIO: {:.3f}".format(trapezium))
print("QUADRADO: {:.3f}".format(square))
print("RETANGULO: {:.3f}".format(rectangle))
