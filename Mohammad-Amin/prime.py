import numpy as np

def is_prime(n):
    for i in range(2, nm):
        if n % i == 0:
            return False

    return True

if n > 10:
    nm = int(np.sqrt(n))
else:
    nm = n

number = int(input("Enter your number: "))
print(is_prime(number))
