#VARIABLES AND STRINGS
name="duncan ndegwa"
print(name.upper()) #to uppercase
print(name.lower()) #to lowercase
print(name.title()) #start with capital letter
#Numbers
marks=72
print(name + str(marks) + "\tis ok")# use str() to represent non sring variabes as strings

#LISTS
car_types=['volvo','subaru','lafesta','toyota','suzuki','lifan']
print(car_types)
print(car_types[-1].title())#lifan starts with a capital -1 for the last element
car_types[0]="tiger" #change/ modify a value volvo to tiger
print(car_types)
#adding an element to a list
car_types.append("swift")
print(car_types)
car_types.insert(0,"mahindra")#inserts at position 0
print(car_types)
#removing elements using del statement
del car_types[0]
print(car_types)
car_types.remove("tiger") #remove is by value not index
print(car_types)
car_types.pop(-1)#  removes the last element
print(car_types)
