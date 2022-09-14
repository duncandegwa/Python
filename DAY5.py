#INPUT FUNCTION
print("Enter your name: ")
name=input()
year=2022
print("Enter your DOB:")
dob=int(input())
if dob>year:
    print("INVALID DOB!!!")
elif dob<1900:
    print(name.upper() + " YOU MUST BE AN AILEN")
else:
    age = year - dob
    print(name.title() + "is" + str(age) + "years old")

#WHILE LOOPS FILLING A DICTIONARY
marks={}
filling=True
while filling:
    student=input("ENTER YOUR NAME?")
    mark=input("marks enter")
    marks[student]=mark #storing data in the dictionary
    repeat=input("press q to quit and any other key to continue")
    if repeat=="q":
        filling=False

for student, mark in marks.items():
    print(student.title() + " got these marks  " + mark)




