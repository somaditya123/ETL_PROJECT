# Characters of symbols
# Immutable
'''
Python ETL Project
name="A"
name2="a"
print(ord(name)) # Unified eqivalant A character - return 65
print(ord(name2))

name="ETL QA LABS"
# Print me all the characters in the string
for ele in name:
    print(ele)

#way 2 to print all the characters in the string
l=len(name)
print("size of the string is :",l)
for idx in range(0,l,1): # It will go index 10 index
    print(name[idx])
'''

# I want to print the string in the reverse order
name="ETL QA LABS"
l=len(name)
start_idx=l-1
end_idx=0
while start_idx>=end_idx:
    print(name[start_idx])
    start_idx=start_idx-1

#write a program to determine whether the string contains any lowercase
name="ETLQALABS"
for ele in name:
    print(ord(ele))
    if (num>97 and num<=122):
        print("There is lower case and that ", chr(num))
        break


