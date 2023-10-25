# Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan.
# Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä
# hissien lukumäärä. Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä.
# Hissien lista tallennetaan talon ominaisuutena. Kirjoita taloon metodi aja_hissiä,
# joka saa parametreinaan hissin numeron ja kohdekerroksen. Kirjoita pääohjelmaan
# lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.
class Elevator:
    def __init__(self, topfloor, bottomfloor):
        self.topfloor = topfloor
        self.bottomfloor = bottomfloor
        self.currently = bottomfloor

    def siirry(self, kerros):
        while self.currently != kerros:

            if self.currently < kerros:
                self.kerrosUp()

            elif self.currently > kerros:
                self.kerrosDown()
        return

    def kerrosUp(self):
        self.currently += 1
        print(f"Hissi nousee kerrokseen: {self.currently}")
        return

    def kerrosDown(self):
        self.currently -= 1
        print(f"Hissi laskeutuu kerrokseen: {self.currently}")
        return

class Building:
    def __init__(self, topfloor, bottomfloor, elevators):
        self.topfloor = topfloor
        self.bottomfloor = bottomfloor
        self.elevators = elevators
        self.elevators = []

    def ajaHissiä(self, elevatorNum, selectfloor):
        return

talo = Building()