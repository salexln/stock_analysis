import argh
from argh.decorators import arg
import numpy as np
import math

"""
taken from: http://stackoverflow.com/questions/509994/best-way-to-write-a-python-function-that-integrates-a-gaussian
"""
def make_gauss(N, sigma, mu):
    k = N / (sigma * math.sqrt(2*math.pi))
    s = -1.0 / (2 * sigma * sigma)
    def f(x):
        return k * math.exp(s * (x - mu)*(x - mu))
    return f

def read_file(path):
	with open(path, 'r') as f:
		lines = f.readlines()

		first  = True
		for line in lines:
			if first:
				first = False
				continue
			
			splitted = line.split(',')

			date = splitted[0]
			
			high = float(splitted[2])
			low = float(splitted[3])
			avg = (high + low) / 2

			# stuff for normal distribution:			
			mu = avg
			# sigma = ((high - avg) + (avg - low)) / 2  #ALEX - is this correct????
			sigma = 1.5
			
			

			# s = np.random.normal(mu, sigma)

			f = make_gauss(2, sigma, mu)

			# find the highest 20%:
			x = high - (high - low) / 5

			print 'low = ', low, ',high = ', high, ',x = ', x, ',mu = ', mu
			
			# make the 
			print 'prediction = ', f(x)			
			print '\n'

			# break






@arg('--data', required = True, help='CSV file with stock data')
def run_stock_analysis(**kwargs):
	path = kwargs['data']
	read_file(path)

if __name__ == '__main__':
	p = argh.ArghParser()
	argh.set_default_command(p, run_stock_analysis)
	p.dispatch()