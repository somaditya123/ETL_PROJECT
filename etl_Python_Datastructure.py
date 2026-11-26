# collection/sequence data types
#list- ordered collection of items,mutable, insertion order preserved
#It can store duplicate values we use []

#tuple- ordered collection of items,immutable, insertion order preserved
#It can store duplicate values we use ()

#set- unordered collection of items,mutable, insertion order not preserved
#It can't store duplicate values we use {}
#list
name_of_student_list = ["somaditya", "ravi", "kishore","somaditya","Thomson","somaditya"]
print(name_of_student_list)
'''
for item in name_of_student_list:
    if item == "somaditya":
print(type(name_of_student_list))
# display each elements/items from the list
#print(name_of_student_list[0])
for i in name_of_student_list:
    print(i)

# range() function
for idx in range(0,4,1):
    print(name_of_student_list[idx])

# add some more items "rakesh"
print("before appending to the list")
name_of_student_list.append("Rakesh")
print("After appending to the list")
print(name_of_student_list)
# Remove the items from the list
name_of_student_list.remove("somaditya")
print("Removing from the list")
print(name_of_student_list)
'''
# List slicing
# syntax list_name (startindex: endindex:steps)
print("using slicing operator ", name_of_student_list[0:3:1])

print("using slicing operator ", name_of_student_list[0:3:2])


# Get 3 items from list and store in another list (idx :0,1,2)
ans_list=[]
for item in range(0,3):
    ans_list.append(name_of_student_list[item])
print("ans_list value are: ", ans_list)



name_of_student_tuple = ("somaditya", "ravi", "kishore","somaditya")
print(type(name_of_student_tuple))
# occurence of the items
print(name_of_student_tuple.count("somaditya"))

# no of elements inside the tuple
no_of_ele=len(name_of_student_tuple)
print(no_of_ele)

name_of_student_set1 = {"somaditya", "ravi","Rakesh"}
name_of_student_set2= {"kishore","somaditya","gyan"}
print(type(name_of_student_set1))
name_of_student_set1.add("somaditya")

print(type(name_of_student_set2))

#Union
ans_set=name_of_student_set1.union(name_of_student_set2)
print(ans_set) # It will remove duplicate and merge both the set

# Intersection

ans_set=name_of_student_set1.intersection(name_of_student_set2)
print(ans_set) # Return the common between both the sets

# Difference
ans_set=name_of_student_set1.difference(name_of_student_set2)
print(ans_set) # Return the minus from both the sets

# symmetric Difference
ans_set=name_of_student_set1.symmetric_difference(name_of_student_set2)
print(ans_set) # Return the minus from both the sets

# Get me 1,3,6,7 elements from the list
# get first 3 and last 3 items
list_num=[1,2,3,4,5,6,7,8,9,10]
ans=[]

first_list=list_num[0:3:1]
print(first_list)
last_list=list_num[7:]
print(last_list)
ans=first_list+last_list
print(ans)