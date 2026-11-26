order_amount=[100,200,300,400,500,600,1800]
# add 18% GST and return the modified list
order_amount_gst=[]
for x in order_amount:
    order_amount_gst.append(x+ x*.18)
print(order_amount_gst)

#List comprehension other way to achive the same way
order_amount_gst_list_comprehension=[x+ x*.15 for x in order_amount]
print(order_amount_gst_list_comprehension)

#nested list
#[[1,1,1],[2,4,8],[3,9,27]]

nested_list=[]
for i in range(1,4):
    nested_list.append([1,1**2,i**3])
print(nested_list)
##using list comprehension
nested_list_print=[[1,1**2,i**3] for i in range(1,4)]
print(nested_list_print)

##Flatten list [1,1,1,2,4,8,3,9,27]

flatten_list=[]
for sublist in nested_list:
    for item in sublist:
        flatten_list.append(item)
print(flatten_list)

## same using List comprehension
flatten_sublist_print=[item for sublist in nested_list for item in sublist]
print(flatten_sublist_print)

orders_list = [
    [101, '2023-07-25 00:00:00.0', 11599, 'CLOSED'],
    [102, '2023-07-25 00:00:00.0', 256, 'PENDING_PAYMENT'],
    [103, '2023-07-25 00:00:00.0', 12111, 'COMPLETE']
]
# extract the closed order using list comprehension
closed_order=[order for order in orders_list if order[3]=="CLOSED"]
print(closed_order)

#unpacking
orders=[1, '2013-07-25 00:00:00.0', 11599, 'CLOSED']
order_id=orders[0]
order_date=orders[1]
customer_id=orders[2]
order_status=orders[3]

#Instead of these multiple lines we can say the below codes

order_id,order_date,customer_id,order_status=orders

## If we want to print any individual data
print(customer_id)

## print range 1-100
number=list(range(1,100))
print(number)

##concat 2 lists
order = [1, "2013-07-25 00:00:00.0", 11599, "CLOSED"]

customer = [
    1,
    "Richard",
    "Hernandez",
    "XXXXXXXXX",
    "XXXXXXXXX",
    "6303 Heather Plaza",
    "Brownsville",
    "TX",
    78521
]

order.append(customer)
print(order)
# In case if you want a flatten list
order.extend(customer)

# what if you want to get the value and respective index from the list value use enumerate
order1 = [1, "2013-07-25 00:00:00.0", 11599, "CLOSED"]

for index,element in enumerate(order1):
    print(f"index is {index},element is {element}")

#count the number of occurence each word

input_list=["hello","Hello","I","am","am","sumit"]
input_set=set(input_list)
print(input_set)
word_count=[input_list.count(word) for word in input_set]
print(word_count)

# Count the number of occurrences of each word

input_text = input("Enter the text: ")

input_list = input_text.split(" ")

input_list_lower = [word.lower() for word in input_list]

input_set = set(input_list_lower)

result_list = []

for word in input_set:
    result_list.append((word, input_list_lower.count(word)))

print(result_list)


