#!/bin/bash
cd all

rm -r 0.* 1* 2* 3* 4* 5* 6* 7* 8* 9* processor* postProcessing log &
wait
decomposePar &
wait
mpirun -np 64 overPimpleDyMFoam -parallel > log &

wait
cd ../
date >> complete.txt