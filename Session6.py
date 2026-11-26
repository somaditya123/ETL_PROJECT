data = """order_id,order_date,order_customer_id,order_status
1,2013-07-25 00:00:00.0,11599,CLOSED
2,2013-07-25 00:00:00.0,256,PENDING_PAYMENT
3,2013-07-25 00:00:00.0,12111,COMPLETE
4,2013-07-25 00:00:00.0,8827,CLOSED
5,2013-07-25 00:00:00.0,11318,COMPLETE
6,2013-07-25 00:00:00.0,7130,COMPLETE
7,2013-07-25 00:00:00.0,4530,COMPLETE
8,2013-07-25 00:00:00.0,2911,PROCESSING
9,2013-07-25 00:00:00.0,5657,PENDING_PAYMENT
10,2013-07-25 00:00:00.0,5648,PENDING_PAYMENT"""

# how many times closed, pending_payment is there
lines=data.split("\n")[1:] # to remove the header [1:]
print(lines)
line_tuple=[tuple(line.split(",")) for line in lines]
#print(line_tuple)
status_list=[line[3] for line in line_tuple]
print(status_list)
input_set=set(status_list)

result_list = []

for word in input_set:
    result_list.append((word, status_list.count(word)))

print(result_list)