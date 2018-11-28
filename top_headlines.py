from flask import Flask, render_template
import requests
from secrets_example import *

app = Flask(__name__)

def get_headline(section):
	baseurl = 'https://api.nytimes.com/svc/topstories/v2/'
	extendedurl = baseurl + section + '.json'
	params = { 'api-key':api_key }
	results = requests.get(extendedurl, params).json()['results']

	return results

@app.route('/')
def index():	
	return '<h1>Welcome!</h1>'

@app.route('/user/<nm>')
def hello_name(nm):
	results = get_headline('technology')
	headlines = []
	for r in results:
		headlines.append(r['title']+' ('+r['url']+')')
	return render_template('user.html', name=nm, my_list=headlines[:5])

@app.route('/user/<nm>/<section>')
def show_headline(nm, section):
	results = get_headline(section)
	headlines = []
	for r in results:
		headlines.append(r['title']+' ('+r['url']+')')
	return render_template('headline.html', name=nm, section=section, my_list=headlines[:5])

if __name__ == '__main__':
	app.run(debug=True)