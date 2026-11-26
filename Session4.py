orders_df = "1,2013-07-25 00:00:00.0,11599,CLOSED"
orders_df_new=orders_df.split(",")
print(orders_df_new) # returns ['1', '2013-07-25 00:00:00.0', '11599', 'CLOSED']
print(orders_df_new[3])
##sequence types -List,Tuple, String
##sequence is not matter- set, dictionary
#Mutable (List, dictionary, set vs Immutable (Tuple )-
#List=[1,2,3] Tuple= (1,2,3) set= {1,2,3} Dictionary= {"brand":"iphone","model":15}

orders_list=['1', '2013-07-25 00:00:00.0', '11599', 'CLOSED']
#mutate the list
orders_list[3]="Completed"
# add a new value to the list
orders_list.append(100)
# if you want to add the value in the specific position like index 1
orders_list.insert(1,100)
# get the length
print(len(orders_list))
#pop() to use the last element from the list
print(orders_list.pop())
print(orders_list)
print(type(orders_list))
print(orders_list[2])

for x in orders_list:
    print(x)

#print sum if number 1 to 11
numbers=range(1,11)
sum=0
for x in numbers:
    sum=sum+x
print(sum)

# print sum number 1 to 11 from input user
range_start=int(input("Please enter the start of the range: "))
range_end=int(input("Please enter the end of the range: "))
numbers=range(range_start,range_end+1)
sum=0
for x in numbers:
    sum=sum+x
print(sum)

#conditional statement to deal with messy data
order_amount=[100,200,None,"Invalid",200.23,300]
sum=0
for x in order_amount:
    if type(x)==int or type(x)==float:
        sum=sum+x
    else:
        continue
print(sum)

order_count_list=[40,40,50,50,50]
print(order_count_list.count(40))
print('-------'*6)
order_count_list.sort()
print(order_count_list)

customer_id=[102,103,102,104,104,105]
# find the list of unique customers
unique_customer_id=[]
for x in unique_customer_id:
    if x in unique_customer_id:
        continue
    else:
        unique_customer_id.append(x)
print(unique_customer_id)
# alternative way of achive this convert the list into set as set doesn't hold the duplicate value

unique_set=set(customer_id)
print(unique_set)


orders_tuple=('1', '2013-07-25 00:00:00.0', '11599', 'CLOSED')
print(type(orders_tuple))

order_count_tuple=(40,40,50,50,50)
print(order_count_tuple.count(50))


