name=input("ENTER YOUR NAME")
mark=input("ENTER YOUR MARKS")
with open('repot.txt','a') as file_obj:
    file_obj.write(name +'.........')
    file_obj.write(mark+"\n")

print("VISIT REPOT.TXT TO PRINTYOUR RESULTS")


