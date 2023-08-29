sukupuoli = input("Käyttäjän biologinen sukupuoli (nainen tai mies): ")
gL = float(input("Käyttäjän hemoglobiiniarvo: "))

nainen = "nainen"
mies = "mies"

if sukupuoli == nainen and gL < 117:
    print("Hemoglobiiniarvo on alhainen.")
elif sukupuoli == nainen and 117 <= gL <= 175:
    print("Hemoglobiiniarvo on normaali.")
elif sukupuoli == nainen and gL > 175:
    print("Hemoglobiiniarvo on korkea.")

elif sukupuoli == mies and gL < 134:
    print("Hemoglobiiniarvo on alhainen.")
elif sukupuoli == mies and 134 <= gL <= 195:
    print("Hemoglobiiniarvo on normaali.")
elif sukupuoli == mies and gL > 195:
    print("Hemoglobiiniarvo on korkea.")

else:
    print("Kirjoitit ehkä nainen tai mies väärin?")
