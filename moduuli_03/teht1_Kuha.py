kuha = float(input("Anna kuhan cm pituus: "))
puuttuvaCm = 37-kuha

if kuha < 37:  # Ennen oli kuha <= 37.
    print(f"Laske kuha takaisin järveen, koska sen tarvii olla {puuttuvaCm} cm pidempi.")
