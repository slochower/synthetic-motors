# Manifest

* `CSD/` - Contains structural coordinates for a second generation Feringa motor (150441) [@doi:10.1126/science.aam8808] from the Cambridge Structural Database. I can't recall the mapping between the deposited coordinates and the sets listed in the SI. I believe that the set listed in the SI do *not* correspond to the motor in Figure 2 of the paper, however. For example, the first descriptor for all the motors in the main text begin with `S` and their quantum scan coordinates all begin with `R`. These isomers should not interconvert. The coordinates in the CSD visually conform to the upper left panel of Figure 2.

* `torsionfit/` - Cloned from https://github.com/choderalab/torsionfit to investigate using `psi4`.

* `torsion-scan/`
    * `scan.in` - Example `psi4` input file to scan the dihedral in increments of 10 degrees (self-contained) with output in `scan.out` after a convergence issue. I investigated this issue only lightly, but I did [raise the point](https://github.com/psi4/psi4/issues/862) with the developers of `psi4` back in November.
    * `generated-from-chaya-torsion-fit/`
        * `torsion-drive.ipynb` - Notebook containing a few helper functions to setup and start `psi4` calculations for fixed scan coordinates (instead of using the built-in `psi4` driver method, like in `scan.in` mentioned above).
        * `B3LYP-torsion-scan/` - Coordinates (`pdb`) and `psi4` input files (`dat`) split into subdirectories by the value of the dihedral.

* `geometry-optimization/`
    * `optimize-with-frozen-dihedral.in` - A test to see if optimizing the initial structure works correctly (in this case: doesn't crash). The title string says "HF/cc-pVDZ" but the commited code is at just "B3LYP/3-21G".
    * `optimize.png` - The results of the optimization.

* `gaussian-torsion-scan-HF-631G/` - Gaussian input (`gjf`) and output (`log`) files for a basic ground state scan of the Feringa motor, using the coordinates specified inside the input file at HF/6-31G without the checkpoint file. Reported total CPU time of 1 day, 17 hours. The scan energies can be pulled from the output file by using GaussView or grepping for the energies: `grep "SCF Done:  E(RHF) =" 1540441.log | awk {'print $5'}` and the scan coordinates: `grep "22,3,5,24" 1540441.log | tail -n +2 | awk {'print $4'}` (note that the scan coordinates need to be wrapped). *Edit:* actually this isn't working at the moment because the log file contains more "SCF Done" entries than I expected, so those are not the final, optimized energies. The energy scan is plotted in `gaussian-torsion-scan.ipynb` and `high-energy.mol2` is one of the high energy conformers.

* `gaussian-torsion-scan-HF-631Gdp/` - Gaussian input (`gjf`) and output (`log`) files for a basic ground state scan of the Feringa motor, using the coordinates specified inside the input file at HF/6-31G(d,p) without the checkpoint file. Reported total CPU time of 5 days, 16 hours. There's a `jupyter notebook` in here that has the energies plotted.

* `gaussian-torsion-scan-excited-HF-631Gdp/` - Gaussian input (`gjf`) and partial output (`log`) files for an excited state scan of the Feringa motor, using the coordinates specified inside the input file at HF/6-31G(d,p) and using keyword `cis(root=1)`. This job didn't finish after 200 hours and the `rwf` scratch file was over 326 GB, so it's probably not the proper way to scan the excited state.