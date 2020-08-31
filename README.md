# UnBlocks-gen: A Python library for 3D Rock Mass Generation and Analysis

A Python 3 library for Discrete Fracture Network construction, 3D block system generation and rock blocks' shape and size analysis. The library constains functions that implement the rock slicing method proposed in C. Boon, G. Houlsby, and S. Utili, “A new rock slicing method based on linear programming,” Computers and Geotechnics, vol. 65, pp. 12 – 29, 2015; and the rock blocks' geometrical analyses described in K. S. Kalenchuk, M. S. Diederichs, and S. McKinnon, “Characterizing block geometry in jointed rockmasses,” International Journal of Rock Mechanics and Mining Sciences, vol. 43, no. 8, pp. 1212 – 1225, 2006.

## License

This library is free software. It is distributed under the terms of the GNU General Public License (GPL), version 3.0 - see the LICENSE.txt file for details.
This library makes use of the Coin-or CLP package, distributed under the terms of Eclipse Public License 1.0 (see https://www.eclipse.org/legal/epl-v10.html for further details).
This library makes use of the Eigen package, distributed under the terms of Mozilla Public License Version 2.0 (see https://www.mozilla.org/en-US/MPL/2.0/ for further details).
This library makes use of the Boost package, distributed under the terms of Boost Software License - Version 1.0  (see https://www.boost.org/LICENSE_1_0.txt for further details).

## Author

- Leandro Lima Rasmussen

Civil and Environmental Engineering Department, University of Brasilia, Brasilia-DF, Brazil.  

leandro.lima@unb.br

## Library structure

The Library consists of three files located in the installation folder: `unblocks.so`, `TriangularPlot.png` and `plotTools.py`. These files should be kept together in the same folder where Python 3 is loaded and run. See `/doc/manual.pdf` for details on the programs functionalities. All source code is under `/src`. Paraview software is recommended for visualizing the VTK files. The `plotTools.py` Python script requires the Matplotlib package for generating the rock blocks' shape and size analysis plots.

Details on how to compile from source and install the library under Ubuntu 18.04 Bionic Beaver and Ubuntu 20.04 Focal Fossa systems can be found in `/doc/Manual.pdf`. For Ubuntu 18.04 Bionic Beaver users, a compiled version of the library is provided in the installation folder. Nevertheless, in case errors appear when importing the library in Python 3, it is recommended that the library be re-compile from source following the instructions provided in the manual.

The examples folder provides three examples illustrating the library usage. Please, check the manual for further information.
