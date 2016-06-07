from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/users', methods=['GET', 'POST'])
def create_user():
   print "Got Post Info"
   # we'll talk about the following two lines after we learn a little more
   # about forms
   name = request.form['name']
   print name
   dojolocal = request.form['dojolocal']
   print dojolocal
   favlang =request.form['favlang']
   print favlang
   commentbox =request.form['commentbox']
   print commentbox
   # redirects back to the '/' route
   return render_template("results.html", name=name, dojolocal=dojolocal, favlang=favlang, commentbox=commentbox)
   #return redirect("templates/results.html")
app.run(debug=True) # run our server
