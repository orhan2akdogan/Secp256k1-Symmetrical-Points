# !pip install ecdsa
# Author: Orhan Akdoğan

PointCount = 141

n = 115792089237316195423570985008687907852837564279074904382605163141518161494337

import matplotlib.pyplot as plt
from ecdsa import SECP256k1
import sympy
import numpy as np

def create_p_and_r(k):
    G = SECP256k1.generator
    P = k * G
    r = P.x() % n
    return P, r, P.x(), P.y()

k_values_mod = [ SECP256k1.order //2 +i - PointCount//2 for i in range(1,PointCount)]
UpPx = []
UpPy = []
UpAnnotate = []
DownPx = []
DownPy = []
DownAnnotate = []
num =0

for k in k_values_mod:
      num = num +1
      if (num<(PointCount/2)):
        P, r, px, py = create_p_and_r(k)
        UpPx.append(px)
        UpPy.append(py)
        UpAnnotate.append(num)
      if (num>(PointCount/2)):
        P, r, px, py = create_p_and_r(k)
        DownPx.append(px)
        DownPy.append(py)
        DownAnnotate.append(num)

plt.figure(figsize=(16, 10))
plt.plot(UpPx, UpPy, marker='o', linestyle='none', color='purple')
plt.plot(DownPx, DownPy, marker='o', linestyle='none', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Secp256k1 Symmetrical Points')
plt.grid(False)
plt.show()
