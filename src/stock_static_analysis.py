import math

import argh
# noinspection PyPackageRequirements,PyUnresolvedReferences
from datetime import timedelta
# noinspection PyPackageRequirements,PyUnresolvedReferences
from datetime import datetime

from argh.decorators import arg


"""
taken from: http://stackoverflow.com/questions/509994/best-way-to-write-a-python-function-that-integrates-a-gaussian
"""
def make_gauss(N, sigma, mu):
	def f(x):
		return 0.5*(1+math.erf((x-mu)/(math.sqrt(2*sigma))))
	return f
"""k = N / (sigma * math.sqrt(2*math.pi))
	s = -1.0 / (2 * sigma * sigma)
	def f(x):
		return k * math.exp(s * (x - mu)*(x - mu))
	return f
"""
def read_file(path, start_date, duration):

	with open(path, 'r') as f:
		lines = f.readlines()

		first  = True
		dict ={}
		buy_price =0
		for line in lines:
			if first:
				first = False
				continue
			
			splitted = line.split(',')

			d = splitted[0]
			date = datetime.strptime(d, "%Y-%m-%d")
			val_open = float(splitted[1])
			high = float(splitted[2])
			low = float(splitted[3])
			val_close = float(splitted[4])
			avg = (high + low) / 2
			end_date= start_date +timedelta(days=duration)
			if start_date <= date< end_date:
				# stuff for normal distribution:
				if start_date==date:
					buy_price=val_open
				if high != low:
					mu = avg
					sigma = ( math.pow(high - avg,2)
							+ math.pow(avg - low,2)
							+ math.pow(val_open - avg, 2)
							+ math.pow(val_close - avg, 2)) / 10

					# sigma = 1.5



					# s = np.random.normal(mu, sigma)

					f = make_gauss(1, sigma, mu)
					dict[date]=f
					# find the highest 20%:
					# x = high - (high - low) / 5
					# x = temp / (high - low)

					# if high != low:
					x = (avg * 1.02 ) #- low) #/ (high - low)

					print 'low = ', low, ',high = ', high, ',x = ', x, ',mu = ', mu, ', date = ', date.strftime ("%d/%m/%Y"), "dict = ", dict.keys()

					# make the
					print 'prediction = ', f(x)
					print '\n'

			# break

	for i in range(-6,7):
		precent = 0.01 * i +1
		new_price = precent*buy_price
		sum_avg=0
		for key in dict.keys():
			result = dict[key](new_price)
			if (i> 0):
				result = 1- result
			sum_avg+=result
		actual_avg = sum_avg/(len(dict))
		print 'precent = ', i, "actual_avg = ", actual_avg, "new_price = ",new_price






@arg('--data', required = True, help='CSV file with stock data')
def run_stock_analysis(**kwargs):
	path = kwargs['data']
	start_date = datetime.strptime("2014-11-20", "%Y-%m-%d")
	duration = 8
	read_file(path,start_date,duration)

if __name__ == '__main__':
	p = argh.ArghParser()
	argh.set_default_command(p, run_stock_analysis)
	p.dispatch()