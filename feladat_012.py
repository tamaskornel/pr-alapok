# be: pozitiv egesz 
# kiír: a szam paros vagy paratlan

szam = int(input("Kérek egy egész számot: "))
if szam % 2 == 0:
    print("A számod {szam} páros!")
else:
    print(f"A számod {szam} páratlan!")

if szam % 2 == 0:
    print("A számod {szam} páros!")
elif szam % 2 == 1:
    print(f"A számod {szam} páratlan!")


