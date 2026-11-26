#####String Operations############
name=("Sumit is very good teacher and he offer's good big data training")
print(len(name))
# indexing helps to get the particular character
# slicing to get the spice of the character
order_status="complete order"
print(order_status[4])
print(len(order_status))
print(order_status[-1])
print(order_status[0:8]) # slicing
print(order_status[9:14])
#print(order_status[9:len(order_status)])
#print(order_status[9:]) print till the end
#print(order_status[:8]) print till the 8th position
# print(order_status[:]) print start to end
# print the last 5 characters
print(order_status[-5:len(order_status)])
# print after the space
index=order_status.find(" ")
print(order_status[index+1:len(order_status)])
#PRINT THE FIRST WORD BEFORE THE SPACE
index=order_status.find(" ")
print(order_status[0:index])

#print every alternative character
print(order_status[0:9:2]) # by default step size is 1

# reverse a string
print(order_status[::-1]) # here step size is -1
# index returns the 1st occurence of (if not found throw exception)
print(order_status.endswith("order"))
print(order_status.capitalize())
print(order_status.replace("complete","completed"))