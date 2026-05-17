import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def plot_P_vs_k(k_max, M_fixed, c_list):
    """
    Plot privacy measure P vs local encoding dimension k for multiple off-diagonal correlations.
    
    Parameters:
    - k_max: maximum k value
    - M_fixed: fixed number of nodes M
    - c_list: list of off-diagonal correlation values
    """
    k_values = np.arange(1, k_max + 1)
    
    colors = cm.coolwarm(np.linspace(0, 1, len(c_list)))
    
    plt.figure(figsize=(8, 5))
    
    for c_offdiag, color in zip(c_list, colors):
        # In the symmetric simplified model, P does NOT depend on k
        P_values = np.full_like(k_values, (1 + (M_fixed - 1) * c_offdiag) / M_fixed, dtype=float)
        
        plt.plot(k_values, P_values, marker='o', color=color, linewidth=2,
                 label=f"$c = {c_offdiag}$")
    
    plt.xlabel(r"$k$", fontsize=20)
    plt.ylabel(r"$P$", fontsize=20)
    
    plt.ylim(0, 1.25)
    plt.xticks( fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(fontsize=12, title="Off-diagonal correlation", title_fontsize=12)
    plt.tight_layout()
    
    plt.savefig("P_k.pdf")

#%%

# parameters
k_max = 10          # vary local encoding dimension k from 1 to 20
M_fixed = 10        # fix number of nodes
c_list = [0.0, 0.2, 0.5, 0.8]

# call the function
plot_P_vs_k(k_max, M_fixed, c_list)