luokka = input("Mitkä näistä LUX, A, B ja C on laivan hyttiluokkasi: ")
luxHytti = "LUX"
aHytti = "A"
bHytti = "B"
cHytti = "C"

if luokka == luxHytti:
    print("LUX on parvekkeellinen hytti yläkannella.")
elif luokka == aHytti:
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif luokka == bHytti:
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif luokka == cHytti:
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka. Kirjoita LUX, A, B ja C isolla että se toimisi.")
