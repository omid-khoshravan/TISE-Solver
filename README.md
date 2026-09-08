# TISE-Solver
Solving the one-dimensional time-independent Schrödinger equation numerically.

This project uses the finite-difference method to solve the time-independent Schrödinger equation numerically, and obtain the corresponding energy eigenvalues and eigenstates for two one-dimensional potentials: the quantum harmonic oscillator and a symmetric quartic double well potential.
## Method
The spatial domain is discretized using a finite-difference approximation. This converts the time-independent Schrödinger equation into a matrix eigenvalue problem, with the Hamiltonian constructed from the kinetic and the potential terms. The Hamiltonian matrix is then passed to 'scipy.linalg.eigh', which solves for its energy eigenvalues and its eigenfunctions.
