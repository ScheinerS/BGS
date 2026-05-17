#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 19:35:26 2026

@author: santiago
"""

import numpy as np
import matplotlib.pyplot as plt

def P_pred(M, k):
    return (1/k) + (1/M)*(1 - 1/k)

Ms = np.arange(2, 31)
ks = np.arange(1, 11)

P = np.zeros((len(ks), len(Ms)))

for i, k in enumerate(ks):
    for j, M in enumerate(Ms):
        P[i, j] = P_pred(M, k)

plt.figure()
plt.imshow(
    P,
    aspect='auto',
    origin='lower',
    extent=[Ms[0], Ms[-1], ks[0], ks[-1]]
)

plt.colorbar(label="P_pred(M,k)")
plt.xlabel("M")
plt.ylabel("k")
plt.title("Predicted privacy landscape")

plt.savefig("P_pred_heatmap.png", dpi=300)
plt.show()