#kuukausi = int(input("Anna kuukauden numero: "))
#vuodenAjat = ("talven", "talven", "kevään", "kevään", "kevään", "kesän", "kesän", "kesän", "syksyn", "syksyn", "syksyn", "talven")
#vuodenAika = vuodenAjat[kuukausi-1]
#print(f"Antamasi kuukausi kuuluu {vuodenAika} vuodenaikaan.")

kuukausiNum = int(input("Anna kuukauden numero: "))
vuodenajat = ("kevään", "kesän", "syksyn", "talven")

if 1 <= kuukausiNum <= 2 or kuukausiNum == 12:
    vuodenaika = vuodenajat[3]
elif 3 <= kuukausiNum <= 5:
    vuodenaika = vuodenajat[0]
elif 6 <= kuukausiNum <= 8:
    vuodenaika = vuodenajat[1]
elif 9 <= kuukausiNum <= 11:
    vuodenaika = vuodenajat[2]

print(f"Antamasi kuukausi kuuluu {vuodenaika} vuodenaikaan.")