# Do-the-homework script
# run this script to generate all the figures in the report. 

# import packages
import numpy as np
import mandelbrot as mb
import millikan as mk

## First Problem: Mandelbrot sets
def doFirstProblem():
	# set parameters
	n_grid_low = 40
	n_grid_high = 2000

	# generate low resolution Mandelbrot grid
	G = mb.mandelbrotGrid(n_grid_low)

	# plot low resolution grayscale
	mb.plotMandelbrotGray(G, n_grid_low)

	# generate high resolution Mandelbrot grid
	G = mb.mandelbrotGrid(n_grid_high)

	# plot high resolution grayscale
	mb.plotMandelbrotGray(G, n_grid_high)

	# plot high resolution colored
	mb.plotMandelbrotColored(G, n_grid_high)

	# plot high resolution colored in log scale
	mb.plotMandelbrotLog(G, n_grid_high)

## Second Problem: Photoelectric effect
def doSecondProblem():
	data_matrix = mk.loadData()
	mk.plotMillikan(data_matrix)

# Do homework problems
doFirstProblem()
doSecondProblem()




