import math
import random

# ≈ <-- toimiiko tämä edes?
# n / N ≈ math.pi / 4
# math.pi ≈ 4n / N

N = int(input("Kuinka monta pistettä laitetaan: "))
kerrat = 0
n = 0  # ympyrän sisällä olevat pisteet

while kerrat <= N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    laskenta = math.sqrt(x ** 2 + y ** 2)

    if laskenta < 1:
        n += 1

    kerrat += 1

pii = 4 * n / N
print(f"π likiarvoksi tuli: {pii:.2f}")
