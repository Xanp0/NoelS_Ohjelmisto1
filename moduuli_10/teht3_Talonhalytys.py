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
        #print("Siirtymämatka tehty.")
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
        self.elevators = []
        for i in range(elevators):
            hissi = Elevator(self.topfloor, bottomfloor)
            self.elevators.append(hissi)

    def ajaHissiä(self, elevatorNum, selectfloor):
        hissi = self.elevators[elevatorNum]
        hissi.siirry(selectfloor)
        print(f"Hissin {elevatorNum+1} siirtymämatka tehty.")
        return

    def paloHälytys(self):
        for i in self.elevators:
            i.siirry(self.bottomfloor)
            if i.currently == i.bottomfloor:
                print(f"Hissi palasi alimpaa kerrokseen, koska palohälytys on päällä.")
        return

talo = Building(7, 0, 3)
talo.ajaHissiä(0, 2)
talo.ajaHissiä(1, 5)
talo.ajaHissiä(2, 1)
talo.paloHälytys()
