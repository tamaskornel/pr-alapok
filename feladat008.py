

jegy = int(input("Kérek egy jegyet 1-5 :"))
if jegy == 5:
    print(f"A jegyed {jegy} jeles")
elif jegy == 4:
    print(f"A jegyed {jegy} jó")
elif jegy == 3:
    print(f"A jegyed {jegy} közepes")
elif jegy == 2:
    print(f"A jegyed {jegy} kettes")
elif jegy == 1:
    print(f"A jegyed {jegy} elégtelen")
else:
    print(f"a jegyed {jegy}, ami nem megfelelő.")
    
