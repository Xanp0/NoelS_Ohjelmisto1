vuosi = int(input("Vuosiluku: "))

if vuosi % 400 == 0 and vuosi % 4 == 0 or vuosi % 100 != 0:
    print(str(int(vuosi)) + " on karkausvuosi.")
else:
    print(str(int(vuosi)) + " ei ole karkausvuosi.")
