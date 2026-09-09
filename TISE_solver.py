import numpy as np
from scipy import linalg

def solve_tise(x_min, x_max, N, V, hbar, m):
    '''
    Solving the oen-dimensional time-independent Schrödinger equation,
    using a finite difference approximation.
    
    Parameters
    ----------
    x_min : float
        Lower boundary of the spatial domain.
    x_max : float
        Upper boundary of the spatial domain.
    N : int
        Number of grid points.
    V : callable
        Potential energy function, V(x).
    hbar : float
        Reduced Planck constatnt.
    m : float
        Mass of the particle.

    Returns
    -------
    x : numpy.ndarray
        Spatial grid points.
    E : numpy.ndarray
        Eigenenergies.
    psi:
        Eigenstates corresponding to the eigenenergies.
    '''

    #creating the spatial grid
    x = np.linspace(x_min, x_max, N) 
    dx = x[1] - x[0] 

    #constructing the kinetic energy matrix
    a = hbar ** 2 / (2 * m * dx ** 2)

    T = (
        2 * a * np.eye(N)
        - a * np.diag(np.ones(N-1), 1)
        - a * np.diag(np.ones(N-1), -1)
    )

    #constructing the potential energy matrix
    V = V(x)
    V = np.diag(V)

    #constructing the Hamiltonian matrix
    H = T + V

    #solving the eigenvalue problem
    E, psi = linalg.eigh(H)

    return x, E, psi