#READING A FILE
with open('F:\Certificates\jk.txt') as file_object:
    contents=file_object.read()
    contentsK = file_object.readlines()
    for line in contentsK:
        print(line)
    print(contents)
    search=""
    for line in contentsK:
        search+=line.rstrip()
    print(len(search))

with open('Ffile.txt','a') as file_obj: #'a' for append 'w' for write 'r' read
    file_obj.write("waigueu")
