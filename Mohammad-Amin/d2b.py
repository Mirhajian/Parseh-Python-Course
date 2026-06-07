n = 54
temp = 0
power = 1

while n > 0:
    temp = temp + ((n % 2) * power)
    power = power * 10
    n = n // 2

print ("TEMP: ", temp)
