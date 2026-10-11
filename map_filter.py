# def square(number):
#     return number*number

# numbers =[1,2,3,4,5]

# result = map(square,numbers)

# print(list(result))



# def double(number):
#     return number * 2

# numbers = [10, 20, 30, 40]

# result = list(map(double, numbers))
# print(result)

# names = ["dipali", "siddhi", "avanti"]
# result = list(map(str.upper, names))
# print(result)\

numbers = [10, 15, 20, 25, 30]
result = list(filter(lambda x: x > 20, numbers))
print(result)