print("Hello World")
# comments in python
a = 14
b=15
print(a)

#list in python
fruits = ['apple', 'banana', 'cherry']
print(fruits)

#lists are ordered mutable collection

#accessing list items using index
print(fruits[0])
print(fruits[2])

#mixed list
mixed_list=[1,2,"kashif", 4.5, True]
print(mixed_list)

#list within list
list_within_list=[12,34,[1,3,3], "kashif", [12.34,45], False]
print(list_within_list)
print(mixed_list[-1])
print(mixed_list[2:4:-1])

#modifying list
#addin an element
list_within_list.append("ibtisam")
print(list_within_list)
#updating the element
list_within_list[2]='replace'
print(list_within_list)
#insert item at specific position
list_within_list.insert(4, "replace 2")
print(list_within_list)
#removing an item
list_within_list.remove("replace 2")
print(list_within_list)
#removing last item
list_within_list.pop()
print(list_within_list)

#removing item at specific position
list_within_list.pop(3)
print(list_within_list)

list2=[1, "kalim", "kalim", 5]
list2.remove("kalim")
print(list2)
print(list2[1])
print(list2.index("kalim"))
print(list_within_list.count(34))

list3=[1,2,6,4,7,9]
list3.sort()
print(list3)
list3.reverse()
print(list3)

abcd=56
print(abcd) 
g=66
print(g)








