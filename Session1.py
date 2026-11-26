
instructor_name = "Sumit Mittal" # String
#course_fee = 800                # Integer
course_rating = 4.95            # Float
is_starting_soon = True         # Boolean
total_income = None             # NoneType

print(type(instructor_name))
#print(type(course_fee1))
print(type(course_rating))
print(type(is_starting_soon))
print(type(total_income))

instructor_name = "Sumit Mittal" # String
course_fee = "800"                # Integer
course_rating = 4.95            # Float
is_starting_soon = True         # Boolean
total_income = None             # NoneType

print(type(course_fee))
course_fee2=int(course_fee)+(int(course_fee) * .1)
print(course_fee2)

#############String concat###########
first_name = "Sumit"
last_name = "Mittal"
print(first_name+' '+last_name)
print("-------"* 7)
print(f"My first name is {first_name} and my last name is {last_name}")

###################Take an input from the user ##############
salary= input("Enter your salary: ")
hike =input("Enter your hike: ")
new_salary= int(salary) + (int(salary) * int(hike)/100)
print(new_salary)