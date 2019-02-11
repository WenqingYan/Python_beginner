# Gnuradio Lesson 7 - 2 vectors average and plot
import cmath
from matplotlib.pylab import *
tau = 2 * pi
def average(readings):
	base = e ** (1j * tau / 360)
	total = 0
	for r in readings:
		v = r[1] * base ** r[0]
		total += v
		arrow(0, 0, v.real, v.imag, head_width=0.05, head_length=0.05, fc='r', ec='r')
	result = total / len(readings)
	arrow(0, 0, result.real, result.imag, head_width=0.05, head_length=0.05, fc='b', ec='b')
	xlim((-1.5, 1.5))
	ylim((-1.5, 1.5))
	ylabel('Imaginary')
	xlabel('Real')
	return (cmath.log(result, base).real, abs(result))
