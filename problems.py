#Write a Python program that takes a number from the user and checks whether it is even or odd.

# number = int(input("Enter a number: "))

# if number%2==0:
#         print("number is even ", number)
# else:
#         print("number is odd ",number)    


#write a Python program that:Takes two numbers from the user Finds which number is larger Prints the larger number
# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))

# if number1 > number2:
#     print("Larger number is:", number1)

# elif number2 < number1:
#        print("Larger number is:", number2) 
# else:
#       print("both are equal")
    

#write armstrong number logic 
# number =153
# copyNumber=number
# sum=0
# remainder=1

# while number > 0:
#     remainder = number%10
#     sum = sum+remainder*remainder*remainder
#     number =number//10
# if copyNumber == sum:
#     print("number is armstrong")
# else :
#     print("number is not armstrong")

#print 1 to 5
def print_numbers(n):
    if n > 5:
       return
    print (n)

    print_numbers(n+1)
print_numbers(1)    