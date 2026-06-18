# Python Arrays
# آرایه های پایتون

# 1. List (لیست)
# لیست یک نوع آرایه قابل تغییره

fruit = [ "Apple", "Banana", "Pineapple", "watermelon", "grape", "mango", "peach"]

print( fruit[0] )
print( fruit[2] )

# چطوری یک میوه جدید به سبد اضافه کنیم
fruit.append("Orange")
print(fruit)

# چطوری یک میوه از سبد حذف کنیم
fruit.remove("Pineapple")
print(fruit)

# چطوری یک میوه به سبد اضافه کنیم
fruit.append("mango")
print(fruit.count("mango"))

# تعداد میوه های توی سبد
print(len(fruit))

# 1. Tuple (توپل)

days = ("Monday", "Tuesday", "Wednsday", "Thursday", "Friday", "Saturday", "Sunday")
print(days)

print( days[0] )

print( len(days) )

# 3. Set (ست)
# تکراری ها رو حذف میکنه

numbers = {1, 2, 3, 3, 4, 5, 5, 5, 6}
print(numbers)

numbers.discard(2)
print(numbers)

# 4. Dictionary (دیکشنری)
# Key : Value
# مقدار : کلید
# مثل کتاب دیکشنری انگلیسی، هر کلمه یه معادل داره

student = { "firstname": "MohammadReza", "lastname": "Baqeri", "age": 10}
print( student["firstname"] )
print( student["age"] )


# چطوری یک مقدار یک کلید رو عوض کنیم
student["age"] = 15
print(student)

# چطوری یک کلید و مقدار جدید اضافه کنیم
student["city"] = "Tabas"
print(student)

print(student.keys())

print(student.values())