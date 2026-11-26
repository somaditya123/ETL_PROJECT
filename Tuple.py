# 1 Create tuple using tuple function
list=[10,20,30,40,50]
t=tuple(list)
print(t)
print(type(t))

# using tuple range function
t1=tuple(range(1,20))
print(t1)
print(type(t1))

# 2. Accessing the element of the tuple using slice operator
t3=(10,20,30,2,6,6,8)
print(t3[2:4])
print(t3)
# using index
print(t3[4])

# 3. Mathematical Operators for Tuple
t4=(10,20,30,2,6,6,8)
t5=(13,20,30,2,6,6,8)
t6=t4+t5
print(t6)

# 4 Tuple packing and unpacking
a=10
b=20
c=30
d=40
e=50
f=60
g=70
h=80
t7=a,b,c,d,e,f,g,h
print(t7)
t8=(10,20,30,2,6,6,8)
a,b,c,d,e,f,g=t8
print("a=",a,"b=",b,"c=",c,"d=","e=",e,"f=",f,"g=",g)

# Write a Program to take a Tuple of Numbers from the Keyboard
     #and Print its Sum and Average?
t9=eval(input("Enter the tuple number:"))
#get the length of the tuple
l=len(t9)
sum=0
for i in t9:
    sum=sum+i
print("The sum is: ",sum)
print("The average number is:",sum/l)


