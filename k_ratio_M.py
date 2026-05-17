import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import MaxNLocator

# Enable LaTeX rendering
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.size": 14
})

def P_pred(M, k):
    return (1/k) + (1/M)*(1 - 1/k)

Ms = np.arange(2, 200)

# Candidate scaling laws
k_scalings = {
    r"$k=M$": lambda M: M,
    r"$k=M/5$": lambda M: M/5,
    r"$k=M/10$": lambda M: M/10,
    r"$k=M/20$": lambda M: M/20,
    r"$k=M/100$": lambda M: M/100,
}

plt.figure(figsize=(8,5))

# Red → blue
colors = cm.coolwarm_r(np.linspace(0, 1, len(k_scalings)))

for (label, kfun), color in zip(k_scalings.items(), colors):

    vals = []

    for M in Ms:
        k = kfun(M)

        # enforce integer k
        k = max(1, int(round(k)))

        vals.append(P_pred(M, k))

    plt.plot(
        Ms,
        vals,
        color=color,
        linewidth=2,
        label=label
    )

plt.xlabel(r"$M$")
plt.ylabel(r"$P_{\mathrm{pred}}(M,k(M))$")
plt.title(r"Privacy scaling under different $k(M)$")

# Integer axis ticks only
plt.gca().xaxis.set_major_locator(
    MaxNLocator(integer=True)
)

plt.legend(loc="upper right")
plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig("k_ratio_M.pdf", bbox_inches="tight")
plt.show()