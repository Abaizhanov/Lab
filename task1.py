print("Hello, World!")

if 5 > 2:
 print("Five is greater than two!")
if 5 > 2:
        print("Five is greater than two!")

#This is a comment
print("Hello, World!")

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = 5
y = "John"
print(x, y)

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

x = 1    # int
y = 2.8  # float
z = 1j   # complex

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

b = "Hello, World!"
print(b[-5:-2])

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

a = "Hello"
b = "World"
c = a + " " + b
print(c)

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

txt = "We are the so-called \"Vikings\" from the north."

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

a = 33
b = 200
if b > a:
  print("b is greater than a")

  a = 33
  b = 33
  if b > a:
      print("b is greater than a")
  elif a == b:
      print("a and b are equal")

a = 200
b = 33
if b > a:

  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

a = 2
b = 330
print("A") if a > b else print("B")

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

    a = 33
    b = 200

    if b > a:
        pass