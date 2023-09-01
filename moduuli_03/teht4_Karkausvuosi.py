vuosi = int(input("Vuosiluku: "))

if vuosi % 400 == 0 or vuosi % 4 == 0 and vuosi % 100 != 0:  # Ennen oli "or" ja "and" väärällä kohdalla.
    print(str(int(vuosi)) + " on karkausvuosi.")
else:
    print(str(int(vuosi)) + " ei ole karkausvuosi.")
