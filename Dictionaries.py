# Create dictionaries
d=dict() # empty dictionaries
# we can add the entries in the dict()
d[100]="durga"
d[200]="ravi"
d[300]="somaditya"
print(d)
#Accessing the data from dictionaries
d1={100:"durga",200:"shiva",300:"ganesh",400:"shiridi sai baba"}
print(d1[100])
print(d1[200])
print(d1[300])
print(d1[400])

#Updating the key value in the dictionaries
d2={100:"durga",200:"shiva",300:"ganesh",400:"shiridi sai baba"}
d2[500]="Hanuman Ji"
d2[500]="Hanuman Jii"
print(d2)

# len() to get the length of the dictionaries
d3=len(d2)
print(d3)

# To get the value of specific keys
print(d2.get(100))
print(d2.get(200))
print(d2.get(300))
print(d2.get(400))
print(d2.get(500))

# items() To get the corresponding key value pair details
for k,v in d2.items():
    print(k,v)
#Write a Program to take Dictionary from the Keyboard
     #and print the Sum of Values

d3=eval(input("enter the dictionaries values"))
sum1=sum(d3.values())
print(sum1)

# Dictionaries comprehension
#SQUARE
d4={x:x*x for x in range(1,10)}
print(d4)
#DOUBLE
d5={x:2*x for x in range(1,10)}
print(d5)
