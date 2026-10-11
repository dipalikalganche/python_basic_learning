numbers=[10,20,30,40,50]
print(numbers)
numbers[1]=200

numbers.append(90)
print(numbers)

num1=[10,20,60,50]
num2=[60,40,69,89]
num1.extend(num2)
print(num1)
print(len(num1))

num1.insert(1,15)
print(num1)

num1.remove(20)
print(num1)