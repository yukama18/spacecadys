### SPACE CADYS PRESENTS
# Imaging the Ionosphere through Electron Density
#### By Austen O'Shaughnessy, Conor Brennan, Divya Chari, Satyam Priyadarshi, Yuka Ma

This python script takes the ISS FPMU Summary Plasma Densities and Temperatures data from https://cdaweb.gsfc.nasa.gov/cgi-bin/eval1.cgi. We downloaded the List Data as CSV files.

We retrieve the electron density based on the location and output a 3D image of the Earth and its surrounding ionosphere (e- density) on a color scale using the plotly.graph_objects module.

The map_ionosphere.py script does the following to create the output image

1. Extract longitude, latitude, altitude, and e- density from the raw database

2. Using plotly and a color gradient scale on e-density, create plot.
