# day=4
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print ("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday") 
#     case 7:
#         print("Sunday") 
#     case _:
#         print("invalid....")    
#      
                 
# month=int (input("Enter month number: "))
# match month:
#     case 1:
#         print("January")
#     case 2:
#         print("Fenruary")
#     case 3:
#         print("March") 
#     case 4:
#         print("April")
#     case _:
#         print("not exist")               

#calculator
# n1 = int(input("Enter first number: "))
# n2 = int(input("Enter second number: "))
# operator = input("Enter operator: ")

# match operator:
#     case "+":
#         print("Result:", n1 + n2)
#     case "-":
#         print("Result:", n1 - n2)
#     case "*":
#         print("Result:", n1 * n2)
#     case "/":
#         print("Result:", n1 / n2)
#     case _:
#         print("Invalid operator")

day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")