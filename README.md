# QE_example_calculations

This repository illustrate procedures to run band structure calculation for solids using Quantum Espresso

Procedure to compute band structure:

step 1: "relax" calculation: Get initial geometry of the solid state compound from experimental data and construct geometry optimization of it.

step 2: `scf' calculation: Conduct plain wave based DFT self-consistency field calculations to calculate the total energy and energy eigenvalue for the system,

step 3: `bands' calculation: Evaluate the energy eigenvalue upon the certain assigned path on the edge of first brillouin zone based on scf converged result.

step 4: `bandx' calculation: Generate plottable data from `bands' calculation

Step 5: Using the Python code `band.py` to read in the outputs from `bandx
