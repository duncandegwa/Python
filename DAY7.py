#RETURNING VALUES FROM A FUNCTION
def yourname(fname,lname):
    full= fname+" " + lname
    return full.title()

f=input("first name")
l=input("last name")
myname= yourname(f,l)
print(myname)
#passing a list
def list1(names):
    for name in names:
        print(name.title())
l=['moses','nyutu','kingoere','weru']
print(list1(l))