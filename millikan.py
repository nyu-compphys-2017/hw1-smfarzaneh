# Python 2.7 script
# Computational Physics, Fall 2017
# Homework #1
# S. M. Farzaneh, farzaneh@nyu.edu

# This program fits a line to Millikan's data 
# using least squares method. 

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

def loadData(filename = 'millikan.txt'):
	data_matrix = np.loadtxt(filename)
	# first column: frequency, second column: voltage
	return data_matrix

def calculateExpectedValues(data_matrix):
	x = data_matrix[:, 0]
	y = data_matrix[:, 1]
	N = float(len(x))
	# calculate Ex
	Ex = 1/N*np.sum(x)
	# calculate Ey
	Ey = 1/N*np.sum(y)
	# calculate Exx
	Exx = 1/N*np.sum(x**2)
	# calculate Exy
	Exy = 1/N*np.sum(x*y)

	return Ex, Ey, Exx, Exy

def calculateFitted(data_matrix):
	# calculate slope and y-intercept of fitted line
	
	# calculate expected values
	Ex, Ey, Exx, Exy = calculateExpectedValues(data_matrix)

	# calculate slope m
	m = (Exy - Ex*Ey)/(Exx - Ex**2)

	# calculate y-intercept c
	c = (Exx*Ey - Ex*Exy)/(Exx - Ex**2)

	return m, c

def plotMillikan(data_matrix):
	# plot Millikan data and the fitting line
	
	# initialize and normalize data points 
	freq_data = data_matrix[:, 0]/1e15
	volt_data = data_matrix[:, 1]

	plt.figure(figsize=(3.3, 3.3))
	plt.plot(freq_data, volt_data, 'o')

	# generate fitted line
	grid_points = 100
	step = 1.2*1e15/grid_points
	freq = np.arange(0, 1.2*1e15 + step, step)
	m, c = calculateFitted(data_matrix)
	volt = m*freq + c
	freq = freq/1e15
	plt.plot(freq, volt)
	x = [0, 0.3, 0.6, 0.9, 1.2]
	y = [-4, -2, 0, 2, 4]
	x_label = ['0', '0.3', '0.6', '0.9', '1.2']
	y_label = ['-4', '-2', '0', '2', '4']

	plt.text(0.3, -2, '$m=$' + str(m), fontsize=9)
	plt.text(0.3, -3, '$c=$' + str(c), fontsize=9)
	plt.title('Millikan\'s Photoelectric Data')
	plt.xticks(x, x_label)
	plt.xlabel('Frequency [PHz]')
	plt.yticks(y, y_label)
	plt.ylabel('Voltage [V]')
	plt.gcf().subplots_adjust(left=0.15)
	plt.gcf().subplots_adjust(bottom=0.15)
	filename = 'millikan.pdf'
	plt.savefig(filename)
