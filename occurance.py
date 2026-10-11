list =[10,10,15,20,10,20]
occurance=dict()

for key in list:
    if key in occurance:
      occurance[key]=occurance[key]+1
    else:
       occurance[key]=1
print(occurance)   
    