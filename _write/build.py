from pandas import read_csv
from jinja2 import Environment, FileSystemLoader
import os
from datetime import datetime
import shutil
from distutils.dir_util import mkpath

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
	j2_env = Environment(loader=FileSystemLoader(THIS_DIR),
                         trim_blocks=True)
	url = "http://finviz.com/export.ashx?v=152&f=cap_microover,ind_stocksonly,sh_avgvol_o100,sh_opt_optionshort&ft=4&c="+",".join(map(str,range(68)))
	data = read_csv(url, delimiter=',', index_col='No.')
	data['20day'] = data['20-Day Simple Moving Average'].str.replace('%','').astype(float)
	data['50day'] = data['50-Day Simple Moving Average'].str.replace('%','').astype(float)
	data['200day'] = data['200-Day Simple Moving Average'].str.replace('%','').astype(float)
	today = datetime.now()
	tpl = j2_env.get_template('template.markdown')
	shutil.rmtree(THIS_DIR+"/../_posts/stocks")
	mkpath(THIS_DIR+"/../_posts/stocks")
	for (idx, stock) in data.iterrows():
		output = tpl.render(
			timestamp=today.strftime("%Y-%m-%d %H:%M:%S"),
			stock=stock,
			).encode('utf-8')
		fileName = "%s-%s.markdown"%(today.strftime("%Y-%m-%d"), stock.Ticker)
		#import pdb; pdb.set_trace()
		with open(THIS_DIR+"/../_posts/stocks/%s"%fileName,'w') as f:
			f.write(output)
