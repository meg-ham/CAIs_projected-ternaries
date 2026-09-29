# CAIs_projected-ternaries

## Context
Stolper (1982) introduced specialised ternary diagrams, projected within the CaO–MgO–Al₂O₃–SiO₂ (CMAS) phase space, to allow the plotting of complex refractory bulk compositions and mineral chemistries of Ca,Al-rich inclusions (CAIs), and the better understanding of their liquidus phase relationships. 

>Stolper, E. 1982. Crystallization sequences of Ca-Al-rich inclusions from Allende: An experimental study. Geochimica et Cosmochimica Acta, 46(11), p.2159-2180.

_CAI bulk compositions and crystallisation paths_ are plotted on a spinel-saturated liquidus diagram projected onto the forsterite (Fo) - anorthite (An) – gehlenite (Geh) plane. The coordinates needed to construct this projected ternary and calculate plottable values are available in Stolper (1982); however, these calculations require the use of complex mathematical matrices.

_CAI pyroxene compositions_ cannot be plotted onto the classic pyroxene quadrilateral due to their high abundances of TiO₂. Instead, Stolper (1982) designed a ternary plot on which CAI pyroxene chemistry can be projected from quartz and enstatite onto the plane diopside (Di) – tschermak (Tsch) – Ca-tschermak (Ca-Tsch). The coordinates needed to construct this projected ternary and calculate plottable values are not publicly available; thus, we determined these coordinates using mathematical matrices.

This repository stores the: (1) Excel files used to convert weight percent (wt%) chemistry analyses into plottable values for the bulk composition _(bulk-triplot)_ and pyroxene _(pyroxene-triplot)_ projected ternaries; (2) Python code used to create and plot the associated ternaries. 

## Referencing
If using this code, please reference: ``meg-ham/CAIs_projected-ternaries``

This work is presented in: 
>Hammett, M. 2025. Formation Conditions of Refractory Inclusions in Chondritic Meteorites: A Study of Natural CAIs and Synthetic Analogues. PhD Thesis.

>Hammett, M., Jones, R. H., Tartèse, R., Cowpe, J. and Hughes, L. 2026. Experimental Constraints on Formation Conditions of Compact Type A and Type B CAIs in CV Chondrites. [in review]

## License
The project is licensed under the GNU-v3 license.

## Installation
Installation of the ``ternary`` library is required. However, scripts are short and designed to be adapted and applied to various problems. Python scripts can be downloaded from this repository and integrated into pre-existing scripts where such functionality is required.

## Python Scripts

**_BC-triplot.py**
Generates the ternary diagram projected from spinel-saturated liquidus onto the forsterite (Fo) - anorthite (An) – gehlenite (Geh) plane.

**_pyroxene-triplot.py** 
Generates the ternary diagram projected from quartz and enstatite onto the diopside (Di) – tschermak (Tsch) – Ca-tschermak (Ca-Tsch) plane. 
