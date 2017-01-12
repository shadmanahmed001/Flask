from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key='hellosecretkey'

@app.route('/')
def index():
	# for idx,val in session:
	# 	print idx,val

	if 'counter' in session:
		session['counter']+=1
	else:
		session['counter']=0
	# for key,value in session.items():
	# 	print key, "=", value
	# 	if value== 0:
	# 		value = value+1
	# 	elif value > 0:
	# 		value = value+1
	print session['counter']
	return render_template ('index.html'),

	# session['visit'] = session['visit']


















app.run(debug=True)