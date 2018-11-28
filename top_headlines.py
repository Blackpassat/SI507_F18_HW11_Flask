from flask import Flask, render_template
import requests
from secrets_example import *

app = Flask(__name__)


@app.route('/')
def index():	
	return '<h1>Welcome!</h1>'

@app.route('/user/<nm>')
def hello_name(nm):
	baseurl = 'https://api.nytimes.com/svc/topstories/v2/'
	section = 'world'
	extendedurl = baseurl + section + '.json'
	params = { 'api-key':api_key }
	results = requests.get(extendedurl, params).json()['results']
	headlines = []
	for r in results:
		headlines.append(r['title']+' ('+r['url']+')')
	return render_template('user.html', name=nm, my_list=headlines[:5])

if __name__ == '__main__':
	app.run(debug=True)