#WORKING WITH LISTS
mylist=['python','django','flask','java','c++','ruby','javascript']
mylist.sort()   #sorting
print(mylist)
for language in mylist:
    print(language.title())
for value in range(6):
    print(value)
evevnumbers=list(range(2,20,2))
print(evevnumbers)#list of even numbers
#copying lists
languages=mylist[:]
print(languages)
#tuples ----elements cannot change
rectangle=(34,90)
print(rectangle[0])
for rect in rectangle:
    print(rect)
area = rectangle[0]*rectangle[1]
print("Area",area)