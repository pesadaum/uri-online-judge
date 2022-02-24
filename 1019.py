import math

value = int(input())

tmp = value / (60**2)

hour_dec, hour_int = math.modf(tmp)
min_dec, min_int = math.modf(hour_dec) * 60
sec_dec, sec_int = math.modf(min_dec) * 60

print(hour_dec, min_dec, sec_dec)
print(hour_int, min_int, sec_int)

# mins = int(math.modf(tmp)[1] * 60)


# hours = int(value)

# print(hours, mins, secs)
