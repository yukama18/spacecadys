### SPACE C.A.D.Y.S. PRESENTS
# Imaging the Ionosphere through Electron Density
#### By Austen O'Shaughnessy, Conor Brennan, Divya Chari, Satyam Priyadarshi, Yuka Ma
#### Vancouver, Canada

This Github repository contains our team's work, code, and webpage for the 2022 NASA International Space Apps Challenge on "Calling All Radio Enthusiasts!".

For detailed project submission information, please visit [the official website](https://2022.spaceappschallenge.org/challenges/2022-challenges/radio-enthusiasts/teams/space-cadys/project).

Our repository is split into two directories: `/docs`, and `/netCDFwork`

For our Github webpage, please visit: https://yukama18.github.io/spacecadys/

1. `/docs`: This directory contains a python script (`plot_ionosphere.py`) taking 5 half-days (0:00 GMT to 12:00 GMT) worth of data from the [ISS FPMU Summary Plasma Densities and Temperatures ](https://cdaweb.gsfc.nasa.gov/cgi-bin/eval1.cgi). The organized data (ending in `.csv`)) can be found in the same directory. The script outputs a `index.html` file containing an interactive 3D globe that graphs the ionosphere (based on electron density[m-3]) in a 5-day snapshot. Here is a quick gif to showcase its effects:

![](https://github.com/yukama18/rotating_ionosphere.gif)

2. `/netCDFwork`: In an attempt to quickly visualize the large amounts of ionosphere/electron density data (upwards of 130,000 data points), we created a netCDF4 file from the .csv. The python code was written in an ArcGIS Pro notebook: `create_netCDF.aprx`. The outputted netCDF4 file is also included: `edensity_4day.nc`. Again, the relevant data is collected from the same ISS website from above and can be found in the directory as a `.csv` file. Note that we only used 4 days of data here.
