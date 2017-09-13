# Python 2.7 script
# Computational Physics, Fall 2017
# Homework #1
# S. M. Farzaneh, farzaneh@nyu.edu

# This program visualizes Mandelbrot sets.

# import packages
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def isMandelbrot(complex_const=0j, n_iteration=100, initial_z=0, norm_z=2):
	# Checks if complex_const results a Mandelbrot set. 
	
	# initialize 
	z = initial_z
	result = True

	# iterate 
	for iteration in range(n_iteration):
		# check the norm of z
		if (abs(z) > norm_z):
			result = False
			break
		z_prime = z*z + complex_const;
		z = z_prime;
		

	return result, iteration

def mandelbrotGrid(n_grid=100, xy_lim=2):
	# Generates the grid of complex constants, C, 
	# and assigns values according to isMandelbrot()

	# define the grid points
	x_vec = np.linspace(-xy_lim, xy_lim, n_grid)
	y_vec = np.linspace(-xy_lim, xy_lim, n_grid)
	# x_grid, y_grid = np.meshgrid(x_vec, y_vec)
	# C = x_grid + 1j*y_grid

	# define mandelbrot grid
	G = np.zeros((n_grid, n_grid))

	# assignment
	for i in range(0, n_grid):
		for j in range(0, n_grid):
			result, iteration = isMandelbrot(x_vec[i] + 1j*y_vec[j])
			G[i, j] = iteration

	return G

def plotMandelbrot(n_grid=100):
	# Generates the Mandelbrot plot and saves it.
	plt.imshow(mandelbrotGrid(n_grid))
	plt.savefig("mandelbrot.pdf")

	











