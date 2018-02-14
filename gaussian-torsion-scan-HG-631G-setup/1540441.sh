#!/bin/bash
#PBS -q home
#PBS -N Feringa
#PBS -l nodes=1:ppn=16
#PBS -l walltime=20:00:00
#PBS -o 1540441.out
#PBS -e 1540441.err
#PBS -m abe
#PBS -M slochower@gmail.com
#PBS -V

cd $PBS_O_WORKDIR
module load gaussian
g09 1540441.gjf
