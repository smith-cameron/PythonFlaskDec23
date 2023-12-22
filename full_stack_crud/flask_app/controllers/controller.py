from flask_app import app
#! Notice -> New Imports
from flask import  render_template, redirect, request, session

#< handle root route access
#* Not required -> Project Specific
@app.route('/')
def index():
  print(session['last'])
  return redirect("/render_form")

#< define GET route to render form
@app.route('/render_form')
def render_form():
  print(f"Get Route: {request.form}")
  return render_template("form.html")

# . define POST route to process form data
# . You will need PLURAL `methods=['POST']`  in your `@app.route()` endpoint 
@app.route('/submit_form', methods=['POST'])
def submit_form():
  #  access form data via `request.form` immutable multi-dict
  print(f"Post Route: {request.form}")
  #  the same way we already access dictionary values 
	#  request retrieves the value of the input field.
  #  dict_name['name_field_of_input_as_the_key']
  print(f"Post Route: {request.form['first_name']}")
	#  session['desired_key'] = value to save in session
  #  session['desired_key'] = request.form['text_field_name']
  session['first'] = request.form['first_name']
  session['last'] = request.form['last_name']
  session['age'] = request.form['age']
  session['email'] = request.form['email']
  session['pass'] = request.form['password']
	#  redirect to GET route
  return redirect('/display')

@app.route('/display')
def display():
  print(session['pass'])
  # todo Pass session values to html
    # , in render_template()
    # , directly in html from session
  return render_template('display.html', password = session['pass'], email = session['email'])

@app.route('/clear_session')
def clear_session():
  # . clear all of session
  session.clear()
  # . clear one specific value
  # session.pop('pass')
  return redirect("/")