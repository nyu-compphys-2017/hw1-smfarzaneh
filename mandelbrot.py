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

# figure settings 
font = {'family' : 'Times New Roman',
        'weight' : 'normal',
        'size'   : 9}

matplotlib.rc('font', **font)


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
	# Generates the grid of complex constants, 
	# and assigns values according to isMandelbrot()

	# define the grid points
	x_vec = np.linspace(-xy_lim, xy_lim, n_grid)
	y_vec = np.linspace(xy_lim, -xy_lim, n_grid)

	# define mandelbrot grid
	G = np.zeros((n_grid, n_grid))

	# assignment
	for i in range(0, n_grid):
		for j in range(0, n_grid):
			result, iteration = isMandelbrot(x_vec[j] + 1j*y_vec[i])
			G[i, j] = iteration

	return G

def plotMandelbrotGray(Grid=np.zeros((100, 100)), n_grid=100):
	# plot Mandelbrot grid and save it. 
	step = int(n_grid/4.0)
	x = np.arange(0, n_grid + step, step)
	x_label = ['-2', '-1', '0', '1', '2']
	y_label = ['2', '1', '0', '-1', '-2']
	plt.figure(figsize=(1.65, 1.65))
	plt.imshow(Grid, cmap='Greys')
	title = 'N = ' + str(n_grid)
	plt.title('N = ' + str(n_grid))
	plt.xticks(x, x_label)
	plt.xlabel('x')
	plt.yticks(x, y_label)
	plt.ylabel('y')
	plt.gcf().subplots_adjust(left=0.2)
	plt.gcf().subplots_adjust(bottom=0.22)
	filename = 'mandelbrot_gray_n' + str(n_grid) + '.pdf'
	plt.savefig(filename)

def plotMandelbrotColored(Grid=np.zeros((100, 100)), n_grid=100):
	# plot Mandelbrot grid and save it. 
	step = int(n_grid/4.0)
	x = np.arange(0, n_grid + step, step)
	x_label = ['-2', '-1', '0', '1', '2']
	y_label = ['2', '1', '0', '-1', '-2']
	plt.figure(figsize=(1.65, 1.65))
	plt.imshow(Grid, cmap="hot")
	title = 'N = ' + str(n_grid)
	plt.title('N = ' + str(n_grid))
	plt.xticks(x, x_label)
	plt.xlabel('x')
	plt.yticks(x, y_label)
	plt.ylabel('y')
	plt.gcf().subplots_adjust(left=0.2)
	plt.gcf().subplots_adjust(bottom=0.22)
	filename = 'mandelbrot_colored_n' + str(n_grid) + '.pdf'
	plt.savefig(filename)

def plotMandelbrotLog(Grid=np.zeros((100, 100)), n_grid=100):
	# calculate log10 of the grid
	Grid = np.log10(Grid)
	# plot Mandelbrot grid and save it. 
	step = int(n_grid/4.0)
	x = np.arange(0, n_grid + step, step)
	x_label = ['-2', '-1', '0', '1', '2']
	y_label = ['2', '1', '0', '-1', '-2']
	plt.figure(figsize=(1.65, 1.65))
	plt.imshow(Grid, cmap="hot")
	title = 'N = ' + str(n_grid)
	plt.title('N = ' + str(n_grid) + ', Log scale')
	plt.xticks(x, x_label)
	plt.xlabel('x')
	plt.yticks(x, y_label)
	plt.ylabel('y')
	plt.gcf().subplots_adjust(left=0.2)
	plt.gcf().subplots_adjust(bottom=0.22)
	filename = 'mandelbrot_log_n' + str(n_grid) + '.pdf'
	plt.savefig(filename)




	


	











