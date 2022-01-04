#!/bin/bash
#SBATCH --cpus-per-task=10
#SBATCH --mem-per-cpu=4G
#SBATCH --job-name=LiO2_dos 
export PYSCF_MAX_MEMORY=16000
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
module load bundle-quantum-espresso/6.1

pw.x < scf.in > scf.out
pw.x < bs.in > bs.out
bands.x < bandx.in > bandx.out 
pw.x < nscf.in > nscf.out
dos.x < DOS.in > DOS.out
