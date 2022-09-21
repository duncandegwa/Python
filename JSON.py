import json

name=input("ENTER YOUR NAME")
filename="name.json"
with open(filename,'w') as file_obj:
    json.dump(name,file_obj)
    print("YOUR NAME IS SAVED SUCCESSFULY")
with open(filename) as file_obj1:
    content=json.load(file_obj1)
print("SAVED NAMES" + content)