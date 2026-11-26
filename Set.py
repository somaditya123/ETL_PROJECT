# Creation of set object
s1={10,20,30,40,"Somaditya","som"}
print(s1)
print(type(s1))

# Creation of set using list and range function

l=[10,20,30,40,"Somaditya","som"]
s2=set(l)
print("Second set value is :",s2)
print(type(s2))

s3=set(range(1,100))
print("Third set value is :",s3)

# Empty set vs empty dict
s4={}
print(s4)
print(type(s4)) # This will return <class 'dict'> compulsory need to use set function
s5=set()
print(s5)
print(type(s5))

# Add item to set
s5={10,20,30,40,"Somaditya","som"}
s5.add(100)

# update the set
s={10,20,30,40}
l=[23,13,33,43]
s.update(l,range(3))
print(s)

# copy function
s6={10,20,30,40}
s7=s6.copy()
print(s7)

# Mathematical operation in set

#union operator
s8={10,20,30,40,50}
s9={23,13,43,53,63}
print(s8.union(s9))
print(s8|s9)

# Intersection operator
s10={10,20,30,40,50}
s11={23,13,43,53,63,10,20,30}
print(s10.intersection(s11))
print(s10&s11)

# difference operator

s12={10,20,30,40,50}
s13={23,13,43,53,63,10,20,30}
print(s12.difference(s13))
print(s13-s12)

# set comprehension is possible
s14={x*x for x in range(1,10)}
print(s14)

s15={x*2 for x in range(1,10)}
print(s15)

s16={2**x for x in range(1,10)}
print(s16)

#  Write a Program to eliminate Duplicates Present in the
#       List?

l=eval(input("enter the list value :"))
# convert the list to set which doesn't support duplicate and automatically remove duplicates
s17=set(l)
print(s17)
# approach 2
l1=eval(input("Enter the list value:"))
l2=[]
for x in l1:
    if x not in l2:
        l2.append(x)
print(l2)

# Write a Program to Print different Vowels Present in the
#given Word?
w=input("Enter word to search vowels:")
s18=set(w)
v={'a','e','i','o','u'}
s19=s18.intersection(v)
print("Different vowel present in",w,"are",s19)