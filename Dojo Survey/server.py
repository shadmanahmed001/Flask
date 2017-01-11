from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
	return render_template("index.html")

@app.route('/results', methods=['POST'])
def results():
	print "Got the results!" 
	return render_template('/results.html', name= request.form['name'], dojo_location= request.form['dojo_location'],fav_lang=request.form['language'],comment= request.form['comment'])
	# return redirect ('/results', '{{ name }}, {{ dojo_location }}, {{ language }}, {{ comment }}')



app.run(debug=True)