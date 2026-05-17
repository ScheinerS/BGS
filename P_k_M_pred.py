
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import MaxNLocator
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))

plt.close('all')
# Enable LaTeX rendering
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.size": 14
})

def P_pred(M, k):
    return (1/k) + (1/M)*(1 - 1/k)

Ms = np.arange(2, 21)
ks = [1, 2, 3, 4, 5]

plt.figure(figsize=(7,5))

# Choose colormap:
# coolwarm: blue -> red
# coolwarm_r: red -> blue (reversed)
colors = cm.coolwarm_r(np.linspace(0, 1, len(ks)))

for k, color in zip(ks, colors):
    vals = [P_pred(M, k) for M in Ms]
    plt.plot(
        Ms,
        vals,
        'o-',
        color=color,
        linewidth=2,
        markersize=6,
        label=rf"$k={k}$"
    )

plt.xlabel(r"$M$")
plt.ylabel(r"$P(M,k)$")
# plt.title(r"Predicted privacy scaling")
# plt.xticks(Ms)

plt.legend(loc="center right")
plt.grid(alpha=0.3)
plt.tight_layout()

plt.savefig("P_pred_curves.pdf", bbox_inches="tight")
plt.show()

plt.tight_layout()

# Save before show
plt.savefig("P_pred_curves.pdf", bbox_inches="tight")
plt.show()