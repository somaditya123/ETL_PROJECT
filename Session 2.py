###Artithmetic operator ################
bigdata_fee=800
azure_fee=200
bigdata_enrollment=40
azure_enrollment=20
total_revenue=bigdata_fee*bigdata_enrollment+azure_fee*azure_enrollment
print(f"total revenue is {total_revenue}")
average_order_price=total_revenue/(bigdata_enrollment+azure_enrollment)
print(f"average order price is {average_order_price}")
print(2**3) # left side binding
print(2**3**3) # right side binding
bigdata_fee = bigdata_fee+50 # bigdata_fee += 50
print(bigdata_fee)
#####################ceil Math functions#############
import math
total_sales=20000.67
print(math.ceil(total_sales))
print(math.floor(total_sales))
negative_sales=-19999
print(math.fabs(negative_sales))

##############Conditional statement##############

marks=int(input("Enter your marks: "))

if marks>35:
    print("marks greater than 35")
else:
    print("marks less than 35")

if marks>80:
    print("A grade")
elif marks>=35:
    print("you passed but you didnt secure A grade")
else:
    print("you failed")

############Assignment############
#take 2 inputs age and crime record
age=int(input("Enter you age: "))
crime_detail=input("Enter your crime detail Y/N: ")
if age>18 and crime_detail=="N":
    print("YOU ARE ELIGIBLE")
else:
    print("YOU ARE  NOT ELIGIBLE")

###########String Operation########
name ="Sumit Mittal"
print("Sumit" in name)
