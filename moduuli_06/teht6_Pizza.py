# Matikka pää ei toimi...
def pizzaLasku(halkaisija, hinta):
    tulos = halkaisija + hinta  # mitä tähän pitää laittaa?
    return tulos

halkaisija1 = float(input("Ensimmäisen pizzan halkaisija: "))
hinta1 = float(input("Ensimmäisen pizzan hinta: "))
halkaisija2 = float(input("Toisen pizzan halkaisija: "))
hinta2 = float(input("Toisen pizzan hinta: "))

ekaTulos = pizzaLasku(halkaisija1, hinta1)
tokaTulos = pizzaLasku(halkaisija2, hinta2)

if ekaTulos < tokaTulos:
    print("Ensimmäisen pizzan yksikköhinta on alhaisempi")
elif ekaTulos > tokaTulos:
    print("Toisen pizzan yksikköhinta on alhaisempi")
