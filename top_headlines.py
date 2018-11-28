from flask import Flask, render_template
import requests
import datetime
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
	greeting = ''
	now = datetime.datetime.now()
	morning = now.replace(hour=12, minute=0, second=0, microsecond=0)
	afternoon = now.replace(hour=16, minute=0, second=0, microsecond=0)
	evening = now.replace(hour=20, minute=0, second=0, microsecond=0)
	night = now.replace(hour=23, minute=59, second=59, microsecond=59)
	if now <= morning:
		greeting = 'Good morning'
	elif now > morning and now <= afternoon:
		greeting = 'Good afternoon'
	elif now > afternoon and now <= evening:
		greeting = 'Good evening'
	elif now > evening and now <= night:
		greeting = 'Good night'
	results = get_headline('technology')
	headlines = []
	for r in results:
		headlines.append(r['title']+' ('+r['url']+')')
	return render_template('user.html', greeting=greeting, name=nm, my_list=headlines[:5])

@app.route('/user/<nm>/<section>')
def show_headline(nm, section):
	results = get_headline(section)
	headlines = []
	for r in results:
		headlines.append(r['title']+' ('+r['url']+')')
	return render_template('headline.html', name=nm, section=section, my_list=headlines[:5])

if __name__ == '__main__':
	app.run(debug=True)
	