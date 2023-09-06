# En tajua miten tekisin tehtävän
import math
import random

# math.pi ** 2 / 4
# math.pi / 4

# ≈ <-- toimiiko tämä edes?
# n / N ≈ math.pi / 4
# math.pi ≈ 4n / N

# x**2 + y**2 < 1

A = math.pi * 1 ** 2  # ympyrän pinta-ala
# B = neliö

N = 1000000
kerrat = 0
n = 0  # ympyrän sisällä olevat pisteet

while kerrat <= N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        n += 1

    kerrat += 1

print("π likiarvo: ???")
