#*********Making list*******
my_list=["kashif", 32, 23.29, True, None, "rida", 45625, "kalim"]
print(my_list)

print(my_list[2])
print(my_list[4])
print(my_list[3:6])
print(my_list[1:8:2])

#adding an element in the list
my_list.append("nadeem")
print(my_list)

#replacing an element
my_list[4]="replace"
print(my_list)

#adding an element at specefic position
my_list.insert(3, False)
print(my_list)

#removing an element
my_list.remove("kashif")
print(my_list)

#removing an element at specipic position
my_list.pop(5)
print(my_list)

#arranging elements in ascending order
numbers_list=[3, 67, 45, 90, 87, 67, 80,]
numbers_list.sort()
print(numbers_list)

#counting number of an element


#finding index of an element
print(numbers_list.index(87))