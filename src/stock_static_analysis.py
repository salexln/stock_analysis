import argh
from argh.decorators import arg
import numpy as np



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
			sigma = ((high - avg) + (avg - low)) / 2  #ALEX - is this correct????
			
			print high, low, mu, sigma

			s = np.random.normal(mu, sigma)
			print s


			break






@arg('--data', required = True, help='CSV file with stock data')
def run_stock_analysis(**kwargs):
	path = kwargs['data']
	read_file(path)

if __name__ == '__main__':
	p = argh.ArghParser()
	argh.set_default_command(p, run_stock_analysis)
	p.dispatch()