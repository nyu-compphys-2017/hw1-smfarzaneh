# Do-the-homework script
# run this script to generate all the plots in the report. 

# import packages
import numpy as np
import mandelbrot as mb

## First Problem: Mandelbrot sets

# set parameters
n_grid_low = 40
n_grid_high = 2000

# generate low resolution Mandelbrot grid
G = mb.mandelbrotGrid(n_grid_low)

# plot low resolution grayscale plot
mb.plotMandelbrotGray(G, n_grid_low)

# generate high resolution Mandelbrot grid
G = mb.mandelbrotGrid(n_grid_high)

# plot high resolution grayscale plot
mb.plotMandelbrotGray(G, n_grid_high)

# plot high resolution colored plot
mb.plotMandelbrotColored(G, n_grid_high)

# plot high resolution colored plot in log scale
mb.plotMandelbrotLog(G, n_grid_high)


## Second Problem: Photoelectric effect




