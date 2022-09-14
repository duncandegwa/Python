#if Statements
bikes=['honda','ranger','jingcheng','boxar','lifan','tiger']
for bike in bikes:
    if bike=='honda':
        print(bike.upper())
    else:
        print(bike.title())
tuktuk='Shark'
if tuktuk not in bikes:
    print(tuktuk, " is not a bike")
else:
    print(tuktuk+ "is a bike also")
# elif statement
votes=1110
if votes==0:
    print("you were not vote")
elif votes>100:
    print("attained 50 +1")
else:
    print("lost")
for bike in bikes:
    if bike=='tiger':
        print(bike.title()," is very expensive")
    else:
        print( bike.upper(),"cheap atleast")