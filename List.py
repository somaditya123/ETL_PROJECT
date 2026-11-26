#1. Create empty List object
list0=[]
print(list)
print(type(list))
#2. Create a list
list1=[10,20,30,40,"A","B","C"]
print(list1)
print(type(list1))
#3. Create List using dynamic input
#list3=eval(input("Enter the value:"))
#print(list3)
#print(type(list3))
#4. Create a list using List function
list4=list(range(0,10,2))
print(list4)
print(type(list4))

#5 convert string to list
s="Durgasoftware"
l=list(s)
print(l)
print(type(l))

#6 Covert a string with split function
s1="My am learning python and its is quite interesting"
l1=s1.split()
print(l1)

# 7 Accessing list using slice operator
n=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(n[1:6:2])
print(n[2:8:3])
print(n[1:6:4])
print(n[1:6])
print(n[1:6:2])

# 8. List is mutable we can change the object of the list
p=[10,20,30,40,50]
print(p)
p[3]=777
print(p)

#9. Traversal the element of the list
w= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in w:
    print(x)

#10. To display only the even number
q=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in q:
    if x%2==0:
        print(x)
# 11 To get Information about List
r=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,10,20,2,2,2,2,2]
# To get the length of the list
print(len(r))
# To get the occurence of specified element in the list
print(r.count(10))
print(r.count(2))

#12. Manupulating the list
# Append -Add the item at the end of the list
t=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,10,20,2,2,2,2,2]
t.append("Somaditya")
print(t)
# To add  all elements to list upto 100 which are divisible by 10
ll=[]
for x in range(0,100):
    if x%10==0:
        ll.append(x)
        print(ll)
# insert - insert value in specific position
t.insert(3,777)
print(t)

# extend- To add item from one list to another
order1=["Chicken","Mutton","Fish"]
order2=["RC","KF","FO"]
order1.extend(order2)
print(order1)
print(order2)

# pop() function remove the last element of the list and return
a=[1,2,3,4,5,6,7,8,9,10]
print(a.pop())
print(a)
print(a.pop())
print(a)
# remove the element based on index using pop()
print(a.pop(3))
print(a)

# 13. Ordering element of the list
g=[1,2,3,4,5,6,7,8,9,10]
g.reverse()
print(g)
g.sort(reverse=True)
print(g)

# 14 cloning using slice operator
y=[1,2,3,4,5,6,7,8,9,10]
x=y[:]
x[2]=7777
print(x)

# Cloning using copy function
u=[1,2,3,4,5,6,7,8,9,10]
v=u.copy()
v[4]=8888
print(v)

# Nested list
k=[1,2,3,[1,2,3]]
print(k[3])

# List comprehension
f=[x*x for x in range(0,10)]
print(f)
p=[x*3 for x in range(0,10)]
print(p)
d=[x for x in f if x%2==0]
print(d)

# print the first word of each letter
words = ["Balaiah", "Nag", "Venkatesh", "Chiranjeevi"]
b=[i[0] for i in words]
print(b)

# split each word and identify the corresponding length of the words
words="the quick brown fox jumps over the lazy dog".split()
t=[[w.upper(),len(w)] for w in words]
print(t)

# Write a Program to display Unique Vowels present in the
#      given Word?
vowels=['a','e','i','o','u']
word=input("Enter the word search for vowels")
# declare empty list
found=[]
for c in word:
    if c in vowels:
        found.append(c)
    print(found)