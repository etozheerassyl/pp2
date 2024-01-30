x = 5
y = "John"
print(x)
print(y)

x1 = 4       # x is of type int
x1 = "Sally" # x is now of type str
print(x1)

x2 = str(3)    # x will be '3'
y2 = int(3)    # y will be 3
z3 = float(3)  # z will be 3.0

x4 = 5
y4 = "John"
print(type(x4))
print(type(y4))

x5 = "John"
# is the same as
x5 = 'John'

a6 = 4
A6 = "Sally"
#A will not overwrite a

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x, y)

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

carname = "Volvo"
x = 50