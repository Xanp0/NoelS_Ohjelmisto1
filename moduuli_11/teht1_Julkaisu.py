class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulostaInfo(self):
        print(f"{self.nimi}")
        return

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivuMäärä):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivuMäärä = sivuMäärä

    def tulostaInfo(self):
        super().tulostaInfo()
        print(f"{self.kirjoittaja}, {self. sivuMäärä}")
        return

class Lehti(Julkaisu):
    def __init__(self, nimi, toimittaja):
        super().__init__(nimi)
        self.toimittaja = toimittaja

    def tulostaInfo(self):
        super().tulostaInfo()
        print(f"{self.toimittaja}")
        return

julkaisu1 = Lehti("Aku Ankka", "Aki Hyyppä")
julkaisu2 = Kirja("Hytti n:o 6","Rosa Liksom", "200 sivua")
print("Julkaisun tiedot")
julkaisu1.tulostaInfo()
print("")
print("Julkaisun tiedot")
julkaisu2.tulostaInfo()
