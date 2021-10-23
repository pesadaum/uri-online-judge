name = str(input())
salary = float(input())
total = float(input())

total_with_extra = total * 0.15 + salary

print("TOTAL = R$ {:.2f}".format(total_with_extra))
