#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 20:20:54 2026

@author: santiago
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif"
})

def P(k, M, alpha, beta):
    num = k + M * k**2 * (alpha**2 + beta**2)
    den = M * (k + k**2 * (alpha**2 + beta**2))
    return num / den

# Parameters
alpha = 1.0
beta = 0.0

M_values = [5, 10, 20, 50]  # different network sizes
k_vals = np.linspace(1, 100, 500)

plt.figure(figsize=(8,6))

for M in M_values:
    k_plot = np.linspace(1, M, 300)
    plt.plot(k_plot, P(k_plot, M, alpha, beta), label=f"M={M}")

# plt.xscale("log")
# plt.yscale("log")

plt.xlabel(r"$k$ (qubits per node)", fontsize=20)
plt.ylabel(r"$P$ (privacy)", fontsize=20)
# plt.title("Privacy P vs k for different M", fontsize=20)
plt.legend(fontsize=15)
plt.grid(True)

plt.savefig('P_k.pdf')
plt.show()