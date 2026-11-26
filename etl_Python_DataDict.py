# dictionary- stores key-value pair,unordered,mutable
'''
emp_details={1:"Arjun",2:"somaditya",3:"anjali"}
print(type(emp_details))
print(emp_details)
# I want to access the name of the  emp no 2
print(emp_details[2])
# add the item in the dictionary
emp_details[4]="kajol"
#Update the value of the employee
emp_details[4]="Akash"
# delete empid-2
del emp_details[4]
emp_details.pop(3)
print(emp_details)
'''
##Modified
emp_details={1:"Arjun",2:"somaditya",3:"anjali"}
all_keys=emp_details.keys()
print(type(all_keys)) # dict_keys
all_values=emp_details.values()
print(all_values)
print(emp_details.items())
# print the eno with emp name
for k,v in emp_details.items():
    print(k,v)

#String data type