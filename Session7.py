# Dictionary is mutable. {"one":1,"two":2}
#Mutable keys Like list can not be allowed here like [1,2,3]:"list"
word_dict={"intelligent":"who is really brilliant",
           "Rich":"who has a lot of money",
           "Car":"who has four wheel",
           3:"three",
           (1,2,3):"tuple"}
print(word_dict)
#To access the key value
print(word_dict["intelligent"])
print(word_dict[3])
print(word_dict[(1,2,3)])
#To add the value in the dictionary
word_dict["bike"]="it has two wheel"
print(word_dict)
#To change the existing dictionary
word_dict["Car"]="Four wheel"
print(word_dict)
#A list with tuples
order_data=[(101,10000),(102,20000),(103,30000)]
#If I want to give the order id and get the amount in this case we can convert the list to dictionary and do it
order_dict=dict(order_data)
print(order_dict)
print(order_dict[102])
# To get all the keys, use .keys()
order_keys=order_dict.keys()
print(order_keys)

#To get the all the values
order_values=order_dict.values()
print(order_values)

#To get the keys and values, use items
order_items=order_dict.items()
print(order_items)

#To get the length of the dictionary
length_order_data=len(order_data)
print(length_order_data)

print('---------'*7)

customer_raw='''customer_id,customer_fname,customer_lname,address,city,state,pincode
11599,Mary,Malone,8708 Indian Horse Highway,Hickory,NC,28601
256,David,Rodriguez,7605 Tawny Horse Falls,Chicago,IL,60625
12111,Amber,Franco,8766 Clear Prairie Line,Santa Cruz,CA,95060
8827,Brian,Wilson,8396 High Corners,San Antonio,TX,78240
11318,Mary,Henry,3047 Silent Embers Maze,Caguas,PR,00725'''

#split the header
customer_header=customer_raw.split("\n")[0]
print(customer_header)

#Now customer_header=customer_id,customer_fname,customer_lname,address,city,state,pincode
customer_data=customer_raw.split("\n")[1:]
print(customer_data)

# Customer data=['11599,Mary,Malone,8708 Indian Horse Highway,Hickory,NC,28601', '256,David,Rodriguez,7605 Tawny Horse Falls,Chicago,IL,60625', '12111,Amber,Franco,8766 Clear Prairie Line,Santa Cruz,CA,95060', '8827,Brian,Wilson,8396 High Corners,San Antonio,TX,78240', '11318,Mary,Henry,3047 Silent Embers Maze,Caguas,PR,00725']
customer_dict= {}
for x in customer_data:
    customer_dict[x.split(",")[0]]=tuple(x.split(",")[1:])
print(customer_dict)

# Dictionary comprehension
customer_dict_comprehension={x.split(",")[0]:tuple(x.split(",")[1:]) for x in customer_data}
print(customer_dict_comprehension)

#{'11599': ('Mary', 'Malone', '8708 Indian Horse Highway', 'Hickory', 'NC', '28601'), '256': ('David', 'Rodriguez', '7605 Tawny Horse Falls', 'Chicago', 'IL', '60625'), '12111': ('Amber', 'Franco', '8766 Clear Prairie Line', 'Santa Cruz', 'CA', '95060'), '8827': ('Brian', 'Wilson', '8396 High Corners', 'San Antonio', 'TX', '78240'), '11318': ('Mary', 'Henry', '3047 Silent Embers Maze', 'Caguas', 'PR', '00725')}
#Now we will get the nested data as a key value
nested_dict={}
for key,value in customer_dict_comprehension.items():
    nested_dict[key]={
        "customer_fname":value[0],
        "customer_lname": value[1],
        "address": value[2],
        "city": value[3],
        "state": value[4],
        "pincode": value[5],

    }
print(nested_dict.get("256").get("customer_fname"))