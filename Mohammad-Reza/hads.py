import random

raz = random.randint(1, 20)

number = int(input("یک عدد صحیح بین ۱ تا ۲۰ وارد کن: "))

if raz == number:
    print("آفرین! درست حدس زدی.")
elif raz > number:
    print("حدست از عدد من کوچک تره!")
else:
    print("حدست از عدد من بزرگ تره!")


print("raz: ", raz)
print("hads: ", number)