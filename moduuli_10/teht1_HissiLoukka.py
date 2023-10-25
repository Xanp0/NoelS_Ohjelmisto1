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
        print("Siirtymämatka tehty.")
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
