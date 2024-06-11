# Comparison between NEK5000 and Xcompact3d in terms of performance and accuracy

A numerical experiment was conducted for internal comparison to compare NEK5000 and Xcompact3d code in terms of performance and accuracy. The flow over cylinder at Re=40 was choosen as the benchmark case. Along with accuracy,
the effect of domain size on the accuracy of simulation was tested.

## Contents of the Repository
1. NEK5000 - Input files for along with `.msh` files to redo the simulations for each case and their respective runtime-log file.
2. Xcompact3d - Input files `.i3d` file to redo the simulation for each case and their respective runtime-log file.

## Conclusion from the experiment
From the above comparison, we observe that NEK5000 simulations are more efficient and accurate
in comparison to the Xcompact3D simulations. The accuracy of the NEK5000 simulations can
be improved further by increasing the number of elements near the cylinder body while keeping
the domain big enough such that the far-field boundary condition is achieved. NEK5000 simulations allow mesh refinement in all directions unlike Xcompact3D and hence require less number of
elements to achieve much better accuracy.

![Twin vortices formed for different cases](https://github.com/airwarriorg91/Comparison_NEK5000_and_Xcompact3d/blob/master/tv.png)

## Detailed Report on the experiment
[Report Link](https://github.com/airwarriorg91/Comparison_NEK5000_and_Xcompact3d/blob/master/report/report.pdf)
