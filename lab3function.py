"""
1)
def unci(a):
    return float(a) * 28.3495231
"""
'''
2)
def f(a):
    return (float(a) - 32) * (5 / 9)
'''
'''
3)
def solve(h, l):
    rabbit=(l-(h*2))/2
    chiken=h-(l-(h*2))/2
    return int(rabbit) , int(chiken)
h=int(input())
l=int(input())
print(solve(h,l))
'''
'''
from math import *
def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True 
def filter(arr):  
    new = []
    for i in arr:
        if isPrime(i):
            new.append(i)
    return new
    '''

"""
def all_perms(somestring):
   from itertools import permutations 
   lst = [''.join(p) for p in permutations(somestring)]
   for i in lst:
       print(i)
somestring = input()
all_perms(somestring)
"""

"""
def rev(example):
    exam = example.split()[::-1]
    li = []
    for i in exam:
        li.append(i)
    print(" ".join(li))
example = str(input())
rev(example)
"""

"""
def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            print("True")
            return True
    print("False")
    return False
has_33([1,3,3])
has_33([1,3,1,3])
"""

"""
def spy_game(list):
    for i in range(len(list)-1):
        if list[i]==0 and list[i+1]==0 and list[i+2]==7:
            print("True")
            return True
    print("False")
    return False
spy_game([1,2,3,4,0,0,7])
spy_game([1,2,3,4])
"""

"""
def Volume(radius):
    print( (4/3)*pi*radius)
x = float(input())
Volume(x)
"""

"""
def unique(list):
    new = []
    for i in range(len(list)):
        if list.count(list[i]) == 1:
            new.append(list[i])
        else:
            continue
    for i in new:
        print(i, end = ' ')
unique([1,2,3,1,1,1,1,2,3,4,6,7,5])
"""

'''
def palindrome(words):
    dict = words
    words = words[::-1]
    if dict == words:
        print('Palindrome!')
    else:
        print("Not a palindrome")
x = input()
palindrome(x)
'''

"""
def histogram(list):
    for i in list:
        for x in range(i):
            print('*', end =' ')
        print(end = '\n')
histogram([4, 9, 7])
"""

"""
n = randint(1, 20)
def Guess_the_number():
    print('Hello! What is your name?')
    name  = input()
    count = 0
    print("Well,",name,', I am thinking of a number between 1 and 20.')
    print("Take a guess.")
    print(n)
    c = randint(1, 20)
    if n == c:
         print("Good job,",name,"!" "You guessed my number in  1 guesses!")
         return 
    else :
        for i in range(20):
            c = randint(1, 20)
            if n != c:
               print("Your guess is too low.")
               print("Take a guess.")
               print(c)
            elif n == c:
                count = i+1
                print("Good job,",name,"!" "You guessed my number in", count , "guesses!")
                break
            else:
                continue
Guess_the_number()
"""

