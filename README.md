# QE_example_calculations

This repository illustrate procedures to run plain-wave DFT calculations for solids using Quantum Espresso

Procedure to compute band structure:

step 1: "relax" calculation: Get initial geometry of the solid state compound from experimental data and construct geometry optimization of it.

step 2: `scf' calculation: Conduct plain wave based DFT self-consistency field calculations to calculate the total energy and energy eigenvalue for the system,

step 3: `bands' calculation: Evaluate the energy eigenvalue upon the certain assigned path on the edge of first brillouin zone based on scf converged result.

step 4: `bandx' calculation: Generate plottable data from `bands' calculation

Step 5: Using the Python code `band.py` to read in the outputs from `bandx

Procedure to compute Density of States (DOS):

Step 1: `nscf' calculation: Evaluate the energy eigenvalue based on the k-point grid from scf calculation.

Step 2: `dos' calculation: Integrate over the assign energy interval to generate plottable date of DOS.

Step 3: Using the Python code `dos.py` to read in the outputs from 'dos'
calculation and make a DOS plot.
 
 
 This website: https://www.materialscloud.org/work/tools/qeinputgenerator offers an user friend interface to generate input file of Quantum Espresso
