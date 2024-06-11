#!/bin/bash

#SBATCH -J Nek-re40
#SBATCH -p shared
#SBATCH -n 32
#SBATCH -t 72:00:00
#SBATCH --mail-type=ALL 
#SBATCH --mail-user=gauravxpgupta@gmail.com

#list of modules you want to use, for example
#module load compiler/openmpi/4.0.2
#module load compiler/gcc/10.2.0
#export FC='mpif77'
#expoer CC='mpicc'

#name of the executable
exe=./nek5000

#run the application
mpirun -n $SLURM_NTASKS $exe
