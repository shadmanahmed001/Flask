from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key= "thisisacode"

@app.route('/')
def index():
	import random
	session['random_number']= random.randrange(0, 101)
	print session['random_number']
	return render_template('index.html')

@app.route('/toohigh')
def too_high():
	return render_template('toohigh.html')

@app.route('/toolow')
def too_low():
	return render_template('toolow.html')

@app.route('/justright')
def justright():
	return render_template('justright.html')

@app.route('/process', methods=['POST'])
def process():
	print request.form['thenumber']
	print session['random_number']

	if int(request.form['thenumber'])==session['random_number']:
		return redirect('/justright')
		
	elif int(request.form['thenumber'])<session['random_number']:
		return redirect('/toolow')

	elif int(request.form['thenumber'])>session['random_number']:
		return redirect('/toohigh')


app.run(debug=True)