# 3D Model of Star Distribution based on distance from Earth

## Description
This program creates an interactive 3D model of the spatial distribution of all the stars in the Yale Bright Star Catalog, which contains approximately all 9,000 stars visible to the naked eye from Earth. The stars are displayed in three dimensions by a coordinate transformation from a spherical coordinate system to a cartesian system. 

The main file "Star Distribution 3D model.ipynb" contains the code of the model. When ran, it will display an interactive figure of the 3D distribution of the stars.

In this cartesian system:\
x-axis: towards the vernal equinox\
x-y plane: plane of the celestial equator\
z-axis: towards the north celestial pole

## Libraries
The data from the Yale Bright Star catalog was managed in a pandas data frame. NumPy was used to perform the necessary calculations. Plotly was used to plot the stars in three dimensions.

## Notes
In the case GitHub is having trouble displaying the output of the figure, I have attached an image file '3d model output image' for reference of what the model looks like when the code is run!

## Credits
BSC5P Bright Star Catalog database: https://heasarc.gsfc.nasa.gov/W3Browse/star-catalog/bsc5p.html


