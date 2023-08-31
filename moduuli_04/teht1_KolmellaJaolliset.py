print("Kolmella jaolliset luvut väliltä 1..1000.")
jaolliset = 1

while jaolliset <= 1000:
    if jaolliset % 3 == 0:
        jaettava = jaolliset
        print(f"Kolmella jaollinen: {jaettava}")

    jaolliset = jaolliset + 1
