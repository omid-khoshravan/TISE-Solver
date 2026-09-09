# TISE-Solver
Solving the one-dimensional time-independent Schrödinger equation numerically.

This project uses the finite-difference method to solve the time-independent Schrödinger equation numerically, and obtain the corresponding energy eigenvalues and eigenstates for two one-dimensional potentials: the quantum harmonic oscillator and a symmetric quartic double well potential.
## Method
The spatial domain is discretized using a finite-difference approximation. This converts the time-independent Schrödinger equation into a matrix eigenvalue problem, with the Hamiltonian constructed from the kinetic and the potential terms. The Hamiltonian matrix is then passed to `scipy.linalg.eigh`, which solves for its eigenenergies and its eigenstates.
## Potentials
The time-independent Schrödinger equation is solved numerically for two one-dimensional potentials:
- Quantum Harmonic Oscillator
- Symmetric Quartic Double Well
## Results
For the quantum harmonic oscillator, the numerically solved eigenenergies are in agreement with the analytical expectations.
For the symmetric quartic double well potential, the lower energy levels form near degenerate pairs, and their corresponding eigenstates alternate between even and odd parity.
The full numerical analysis, including the energy spectra and eigenstate plots are in `TISE_Numerical_Solution.ipynb`.
## Reusable Solver
The numerical method used in the notebook is implemented as a reusable function in `TISE_solver.py`. 
