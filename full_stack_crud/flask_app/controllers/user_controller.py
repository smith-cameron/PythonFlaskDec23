from flask_app import app
from flask import  render_template, redirect, request, session
from flask_app.models.user import User

@app.route('/user_form')
def user_form():
  # print("in user_form")
  return render_template("form.html")

@app.route('/submit', methods=['POST'])
def submit():
  print(request.form)
  # Catch form values from post request
  data = {
    'first_name': request.form['first_name'],
    'last_name': request.form['last_name'],
    'email': request.form['email'],
    'password': request.form['password'],
    'age': request.form['age'],
  }
  #  Call model method with insert query
  User.create(data)
  # redirect to a page to display all users
  return redirect('/user_form')

@app.route('/display_all')
def display_all():
  all_users = User.get_all()
  print(f"from controller: {all_users}")
  return render_template("displayAll.html", 
  all_users = all_users,
  # variable = User.get_all()
  )

@app.route('/delete_user/<int:user_id>')
def delete_user(user_id):
  User.delete_one({'object_id':user_id})
  return redirect('/display_all')

@app.route('/update_user/<int:user_id>')
def update_user(user_id):
  return render_template('updateForm.html',
  user = User.get_one({"object_id" : user_id}))

@app.route('/update_user/<int:user_id>', methods=['POST'])
def update_user_post(user_id):
  print(request.form)
  # Catch form values from post request
  data = {
    'first_name': request.form['first_name'],
    'last_name': request.form['last_name'],
    'email': request.form['email'],
    'age': request.form['age'],
    # Add a variable to the date sent with your query
    # This particular variable does not come from the form but rather the URL
    'user_id' : user_id
  }
  #  Call model method with update query
  User.update_one(data)
  # redirect to a page to display all users
  return redirect('/display_all')