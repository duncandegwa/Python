#dictionareis
marks={'john':98,'perte':12,'keter':55}
print(marks['john'])
#Modifying Values in a Dictionary
marks['john']=35
print(marks['john'])
#Removing Key-Value Pairs
del marks['keter']
print(marks)
for mark,point in marks.items():
    print("NAME : " + mark)
    print("MARKS : "  + str(point) )