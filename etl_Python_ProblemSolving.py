#Q1. Given a list, find the count of each element in the list
# e.g. marks =[10,11,12,13,15,10,20,12,15,12]
# o/p = 10--coming  twice, 12 us twice, every number and corresponding counts
#Like 10:2, 11:1, 12:3,15:2  and store in a dictionary
# Create a generic function

def count_dict_count(list1):
    count_marks= {} # declare an empty dictionary
    for ele in list1:
        if ele in count_marks:
            count_marks[ele] = count_marks[ele] + 1  # If it is available then add it 1
        else:

            count_marks[ele]=1
    return count_marks

marks =[10,11,12,13,15,10,20,12,15,12]
ans_dict=count_dict_count(marks)
print(ans_dict)

#Q2.  Can you find the duplicate MARKS in the list and return a list
def getDuplicate_marks(ans_dict):
    duplicate_lst = []
    for keys in ans_dict.keys():
        if ans_dict[keys] > 1:
            duplicate_lst.append(keys)

    return duplicate_lst
ans_list=getDuplicate_marks(ans_dict)
print(ans_list)

#Q3.  Can you get me all the uniqe marks
def getUnique_marks(ans_dict):
    unique_lst = []
    for keys in ans_dict.keys():
        if ans_dict[keys] == 1:
            unique_lst.append(keys)

    return unique_lst
ans_list=getUnique_marks(ans_dict)
print(ans_list)

#Q4.  Can you get me all the uniqe and duplicate marks from the list and return in separe list
def getDuplicate_unique_marks(ans_dict):
    duplicate_lst = []
    unique_lst = []
    for keys in ans_dict.keys():
        if ans_dict[keys] > 1:
            duplicate_lst.append(keys)
        else:
            unique_lst.append(keys)

    return duplicate_lst, unique_lst
ans_list=getDuplicate_unique_marks(ans_dict)
print(ans_list)

# Strings slicing- Extract sub string from a string
city="Banaglore"
# Get the whole strings--Syntax --stringname[startindex:endindex:step]
a=city[::]
print(a)
#get first 4 character
#way 1
for idx in range(0,4,1):
    print(city[idx])
#way2 -slicing
print(city[0:4:1])

# Print every even characters
print(city[0::2])

# Print every odd characters
print(city[1::2])

# print last 4 characters in the city
print(city[-1:-4:-1])

#Print the whole string in reverse
print(city[::-1])

# Split
email="etlqalabs@gmail.com"
print(email.split("@"))

name="Akshay Soni"
name_list=name.split(" ")
print("First name : ",name_list[0])
print("Last name : ",name_list[-1])
