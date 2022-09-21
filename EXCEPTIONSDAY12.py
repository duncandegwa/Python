one=int(input("ENTER FIRST DIGIT:"))
two=int(input("ENTER SECOND DIGIT:"))
try:
    div=one/two
except ZeroDivisionError:
    print("ZERO IS INDIVISIDLE")
else:
    print(div)
filename="repot.txt"       #TRY WITH A FILE THAT DOES NOT EXIST
try:
    with open(filename) as fil_obj:
        content=fil_obj.read()
        print(content)
except FileNotFoundError:
    print("FILE DOES NOT EXIST")


