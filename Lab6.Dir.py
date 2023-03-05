import os
import string

# # 1
# path = 'C:\Users\User\PycharmProjects\Hello\Task'
# dir_list = os.listdir(path)
# print("Only directories:")
# print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))])
# print("\nOnly files:")
# print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name))])
# print('\n')
# print(dir_list)

# # 2
# path = 'C:\Users\User\PycharmProjects\Hello\Task'
# print('Exist:', os.access('path', os.F_OK))
# print('Readable:', os.access('path', os.R_OK))
# print('Writable:', os.access('path', os.W_OK))
# print('Executable:', os.access('path', os.X_OK))

# # 3
# print("Test a path exists or not:")
# path = 'C:\Users\User\PycharmProjects\Hello\Task\Lab6.Dir.py'
# print(os.path.exists(path))
# print("\nFile name of the path:")
# print(os.path.basename(path))
# print("\nDir name of the path:")
# print(os.path.dirname(path))

# # 4
# f = open('newline.txt', 'r')
# cnt = 0
# Includes = f.read()
# CoList = Includes.split('\n')
# for i in CoList:
#     if i:
#         cnt+=1
# print(f"the number of lines: {cnt}")

# # 5
# digit = ['1','2', '3', '4', '5', '6', '7', '8', '9', '10']
# with open('digits.txt', 'w') as f:
#      for i in digit:
#         f.write(f'{i}\n')

# # 6
# if not os.path.exists("letters"):
#    os.makedirs("letters")
# for letter in string.ascii_uppercase:
#    with open(letter + ".txt", "w") as file:
#        file.writelines(letter)

# # 7
# with open('digits.txt',"r") as file:
#      with open('digits_2.txt',"w") as file1:
#           for i in file:
#               file1.write(i)
# content = open("digits_2.txt")
# print(content.read())

# # 8
# path = 'C:\Users\User\PycharmProjects\Hello\Task\Lab6.py\file.txt'
# if os.path.exists(path):
#   os.remove(path)
# else:
#   print("The file does not exist")