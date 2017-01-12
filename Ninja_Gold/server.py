from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key='password'

@app.route('/')
def index():

	if 'gold' in session:
		pass
	else:
		session['gold']  = random.randrange(0,100)

	return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():

	if request.form['hello'] == "farm":
		session['farm_gold'] = random.randrange(10,20)
		session['gold']+= session['farm_gold']
		print request.form['hello']
		return redirect ('/')
	# import random
	elif request.form['hello']=="cave":
		session['cave_gold'] = random.randrange(5,10)
		session['gold']+= session['cave_gold']
		print request.form['hello']
		return redirect ('/')
	# import random
	elif request.form['hello']=="house":
		session['house_gold'] = random.randrange(2,5)
		session['gold']+= session['house_gold']
		print request.form['hello']
		return redirect ('/')
	# import random
	elif request.form['hello']=="cas44ino":
		session['casino_gold'] = random.randrange(-50,50)
		session['gold']+= session['casino_gold']
		print request.form['hello']
		return redirect ('/')




app.run(debug=True)