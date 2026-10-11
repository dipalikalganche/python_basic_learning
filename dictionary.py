student={
    "fname":"Dipali shahaji kokane",
    "roll no":3340,
    "city":"pune"
}

print(student["city"])

student["adress"]="sasanenagar"
print(student)

student["adress"]="kalepadal"
print(student)

# for key in student:
#     print(student[key])

print(student.keys())

del student["city"]
print(student)    

numbers=[10,20,10,30,10]
