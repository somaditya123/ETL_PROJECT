# Variables
'''
nameOfStudent = 'abhinav'
ageOfStudent =25
eligible_for_vote= True
print(nameOfStudent)
print(ageOfStudent)
print(eligible_for_vote)
print("student name is :",nameOfStudent," and age of the student is:", ageOfStudent)
''''''
#Naming convension
#1)Camel case 2) snake case 3)Pascal case
#Type casting (casting one data type to another
age="25"
print("Age is of type : ",type(age))
# Convert the age string to integer
age_converted=int(age)
print(type(age_converted))
mark1="60"
mark2="50"
total_mark_converted=int(mark1)+int(mark2)
print(total_mark_converted)

# Upcasting (Converting lower to higher data type- that means you dont lose anything)
weight_of_person_int=75
print(float(weight_of_person_int))
# and downcasting(Converting higher to lower data type- chances of loosing the data)

weight_of_person_float=75.20
print(int(weight_of_person_int))
'''
# control statements (if..else..elif (else if) )
# if statement
age=96
if age <18:
    print("person is NOT eligible for vote")
elif age>=18 and age <95:
    print("person is  eligible for vote")
else:
    print("person is super senior citizen")

# for loop
# print ETLQALABS 10 TIMES
for val in range(11):
    #print(val)
    print(val, "ETL QA LABS")
print("While loop demo")
# While loop (Exexcute untill is true)
start=1
end=10
while (start<end):
    print(start, "ETL QA LABS")
    start+=1




