# """
# range is used for sequence there are three types of ranges
# 1)Range(stop)
# 2)Range(Start and Stop) and Stop is excluded 
# 3)Range(Start,Stop,Step)

# """
# #Print from 0 to 10
# # for i in range(11):
# #  print(i)

# #print only even numbers from 1 to 20
# # for numbers in range(1,20):
# #   if numbers%2!=0:
# #     print("even numbers ",numbers)
# #   else:
# #     print("number is odd", numbers)

# #take one variable age if age>18 or eqal to 18 means prsonm can vote
# # if less than 18 person can not vote if age ges beypnd 100 then enter valid number 

# Age=0
# Age_limit=100
# Age_minimum=10

# if Age>=18 and Age<=100:
#   print("person can vote")

# elif Age<18 and Age>=0:
#   print("person not eligible to vote bcz age is less")

# else:
#   print("plz Enter valid detail")  

# #continue and break 

# for number in range(1,11):
#    if number<=5:
#      break
#      print(number)

#print 1 to 10 don't print 5 and 7 
# count=0;
# for num in range(1,11):
#   if num==5 or num==7:
#     continue
#   count=count+1
#   print(num)
# print("count",count)
        

# #revesrse the string 
# for num in range(10,0,-1):
#   print(num)

num=1
while num<=10:
    print("number is: " ,num)
    num=num+1
