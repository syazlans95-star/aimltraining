employee= {"id":1,
           "name":"Lan",
           "salary":5000.50}
        

print("Employees Detail as follows:")
for key,value in employee.items():
    print(key, "->", value)

employee["city"]="Kuantan"
print('\nDictionary after adding City\n')

for key,value in employee.items():
    print(key, "->",value)
