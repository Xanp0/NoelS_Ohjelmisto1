# Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
# Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas.
# Uusi hissi on aina alimmassa kerroksessa. Jos tee luodulle hissille h esimerkiksi
# metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös- tai
# kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen.
# Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat,
# missä kerroksessa hissi sen jälkeen on. Testaa luokkaa siten, että teet pääohjelmassa hissin ja
# käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.
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

hissi0 = Elevator(7, 0)
hissi0.siirry(5)
hissi0.siirry(0)
