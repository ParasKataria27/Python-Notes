'''
Data Type:
----------------
1. Numerical Data :- 1.Integer int, 2.Float 3. Complex (21j)

2. Text Type Data :- Strings  str

3. Sequence Data :- List[], tuple(), Range()

List :- List always written in square bracket
x = ["data","Science",343,450.5]

Tuple :- tuple are written in round bracket.
x = ("data","science",343,450.5)

Range() :- it is used to print the number in sequence
range(starting,ending,step_size)
range(1,100,2)

4. Mapping Data :- Dictionary {Key:Values} Dictionary are written in curley bracket
 and pair of key and values.

5. Set Data :- set{} are written in curley bracket.

6. Boolen Data :- True, False

7. None :- None
------------------'''

#Numerical Data
x = 45
y = "Waheguru"
z = 45.65
a = 51j

print(x)
print(type(x))

print(y)
print(type(y))

print(z)
print(type(z))

print(a)
print(type(a))

#How to find the length of a text
#len()

x = "data science"

print(x)
print(len(x))
print(len(x)-1)

x = "12000"
print(len(x))

x = "10"
y = "20"
print(x+y)

x = "data"
y = "science"
print(x)
print(y)


#Forecasting of Data
# It is used to change the data type

x = 456
print(type(x))

y= str(x) #changed into string
print(y)
print(type(y))

print(y*4)

g = "125"
print(type(g))

h = float(g)    #Changed into float
print(type(h))
print(h)

i = complex(g)  #Changed into complex
print(type(i))
print(i)

j = list(g)   #changed into list
print(type(j))
print(j)

k = int(g)   #changd into list
print(type(k))
print(k)