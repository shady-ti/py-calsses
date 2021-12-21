# 1. create a list with numbers from 1 to 100
mylist = []
y = 0

while y != 100:
    y = y + 1
    mylist.append(y)

# print(mylist)

# collections form
shortcut_list = [i for i in range(101)]

# print(shortcut_list)

# 2. create a list with the first 100 cubes using shortcut_list
newlist = [i ** 3 for i in shortcut_list]
# print(newlist)

# 3. list of lists:
# [
#       [1, 2, 3, ..., 50]  (power 1)
#       [1, 4, 9, ...]      (power 2)
#       ...
#                           (power 50)
# ]

list2 = [[number ** power for number in range(51)] for power in range(51)]

# for sublist in list2:
#     print(sublist)
#     print('\n\n\n')

from os import walk

# for each in walk('.\\basic datatypes'):
#     print(each)

# (current folder, list of sub folders, list of files in current folder)
# (str, List<str>)
filepathlist = []

for currentfolderdetails in walk(".\\basic datatypes"):
    currentfolder, listofsub, listoffiles = currentfolderdetails
    for file in listoffiles:
        file_path = currentfolder + "\\" + file
        filepathlist.append(file_path)

# hw: convert to list comprehension


a = [1, 2, 3, 4, 5]
b = a
b[1] = "insert value"
print(a)

c = a.copy()
c[1] = 'insert value'
print(c)

print(a[3])
print(a[-2])

a.insert(2, 'blah')
print(a)