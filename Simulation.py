import numpy as np
from scipy.linalg import expm
import matplotlib.pyplot as plt
from functools import reduce

# Pauli matrices:
I = np.eye(2, dtype=complex)
X = np.array([[0,1],[1,0]], dtype=complex)
Y = np.array([[0,-1j],[1j,0]], dtype=complex)
Z = np.array([[1,0],[0,-1]], dtype=complex)

def kron_all(ops):
    return reduce(np.kron, ops)

# ---------- operator on qubit q ----------
def op_on_qubit(op, q, N):
    ops = [I]*N
    ops[q] = op
    return kron_all(ops)

# ---------- CZ gate ----------
def CZ(i,j,N):
    dim = 2**N
    U = np.eye(dim, dtype=complex)

    for x in range(dim):
        bi=(x>>i)&1
        bj=(x>>j)&1
        if bi and bj:
            U[x,x]=-1
    return U

# ---------- Complete-graph BGS ----------
def make_BGS(M,k):

    N=M*k

    # bundle indexing
    bundles=[]
    c=0
    for i in range(M):
        bundle=[]
        for a in range(k):
            bundle.append(c)
            c+=1
        bundles.append(bundle)

    plus=np.array([1,1],dtype=complex)/np.sqrt(2)
    psi=kron_all([plus]*N)

    U=np.eye(2**N,dtype=complex)

    # complete graph K_M
    for i in range(M):
        for j in range(i+1,M):

            for q in bundles[i]:
                for r in bundles[j]:
                    U=CZ(q,r,N)@U

    psi=U@psi
    return psi,bundles


# Encoding
def H_i(i,bundles,N):

    H=np.zeros((2**N,2**N),dtype=complex)

    for q in bundles[i]:
        H += op_on_qubit(Y,q,N)

    return H


def privacy(M,k):

    psi,bundles=make_BGS(M,k)
    N=M*k

    Q=np.zeros((M,M))

    H=[]

    for i in range(M):
        H.append(H_i(i,bundles,N))

    for i in range(M):
        for j in range(M):

            val=np.vdot(
                psi,
                H[i]@H[j]@psi
            )

            Q[i,j]=4*np.real(val)

    a=np.ones(M)/np.sqrt(M)

    P=(a@Q@a)/np.trace(Q)

    return P

#%%
plt.close('all')

Ms=range(1,3)


results = {}

for k in [1,2,3]:

    vals = []

    for M in Ms:
        print(f"\rk={k}, M={M}", end='')
        P = privacy(M,k)
        vals.append(P)
        
    results[k] = vals

print("\nDone.")

plt.figure()

for k, vals in results.items():

    plt.plot(
        Ms,
        vals,
        'o-',
        label=f'k={k}'
    )

plt.xlabel("M")
plt.ylabel("P")
plt.legend()
plt.grid()

plt.savefig("privacy_all.pdf",dpi=300)