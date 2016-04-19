import argh
from argh.decorators import arg




def read_file(path):
	with open(path, 'r') as f:
		lines = f.readlines()

		for line in lines:
			print line






@arg('--data', required = True, help='CSV file with stock data')
def run_stock_analysis(**kwargs):
	path = kwargs['data']
	read_file(path)

if __name__ == '__main__':
	p = argh.ArghParser()
	argh.set_default_command(p, run_stock_analysis)
	p.dispatch()