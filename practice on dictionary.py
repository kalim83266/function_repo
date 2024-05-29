# creating dictionary using curly braces
person={
    "name" : "kashif",
    "city" : "peshawar",
    "age" : "12"
}
print(person)

# creating dictionary using dict() function
person=dict(name="kashif", city="peshawar", age="12")
print(person)

# accesing elements of dictionary
print(person["name"])
print(person["age"])
print(person["city"])

# adding a new element in dictionary
person["phone_number"]="03018706117"
print(person)

# removing element from dictionary
del person["phone_number"]
print(person)
pop_item=person.pop("name")
print(person)
print(pop_item)