# Python Arrays


# 1. List (لیست), mutable

fruit = [ "Apple", "Banana", "Pineapple", "watermelon", "grape", "mango", "peach"]

print( fruit[0] )
print( fruit[2] )

# * String is a type of list

message = ["h", "e", "l", "l", "o"]
message_string = "hello"

print( message[0] )
print( message_string[0] )

# * How to add a new item to the end of the list:
fruit.append("Orange")
print(fruit)

# * How to remove a item
fruit.remove("Pineapple")
print(fruit)

# * BREAKING NEWS: MOHAMMAD AMIN HAD A DISCOVERY: THIS IS HOW YOU COUNT A ITEM:
fruit.append("mango")
print(fruit.count("mango"))

# * The count of a items in a list
print(len(fruit))

# * How to add another list to an existing one
vegetable = ["Cabbage", "Cucumber", "Tomato", "Carrot"]
print(fruit.extend(vegetable))
print(fruit)


# 2. Tuple, immutable

days = ("Monday", "Tuesday", "Wednsday", "Thursday", "Friday", "Saturday", "Sunday")
print(days)

print( days[0] )
print( days.index("Wednsday") )

print( len(days) )

# 3. Set
# Cannot repeat

numbers = {1, 2, 3, 3, 4, 5, 5, 5, 6}
print(numbers)

numbers.discard(2)
print(numbers)

# 4. Dictionary
# Key : Value

student = { "name": "Alireza", "age": 11, "grade": 18.5}
print( student["name"] )
print( student["grade"] )


student["age"] = 15
print(student)

# Adding a new pair
student["city"] = "Tabas"
print(student)

print(student.keys())

print(student.values())

print(student.get("Tabas"))