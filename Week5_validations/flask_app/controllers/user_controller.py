from flask_app import app
from flask import  render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.car import Car
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/home')
def dashboard():
  if session['user_id']:
    return render_template("dashboard.html",all_users = User.get_all(), all_cars = Car.get_all_join_creator())
  return redirect('/')

@app.route('/user/logout')
def logout():
  session.clear()
  return redirect('/')

@app.route('/user/create', methods=['POST'])
def create_user():
  if User.validate(request.form):
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
      'first_name': request.form['first_name'],
      'last_name': request.form['last_name'],
      'email': request.form['email'],
      'password': pw_hash,
      'age': request.form['age'],
    }
    user_id = User.create_one(data)
    session['user_id'] = user_id
    return redirect('/home')
  return redirect('/')

# todo login routing/method
@app.route('/user/login', methods=['POST'])
def login_user():
  user_in_db = User.get_by_email({'user_email': request.form['email']})
  if user_in_db:
    if bcrypt.check_password_hash(user_in_db.password, request.form['password']):
      session['user_id'] = user_in_db.id
      return redirect('/home')
  flash("Invalid Credentials", "login")
  return redirect('/')

@app.route('/user/delete/<int:user_id>')
def delete_user(user_id):
  if session['user_id']:
    User.delete_one(user_id)
    return redirect('/home')
  return redirect('/')

@app.route('/user/edit/<int:user_id>')
def edit_user(user_id):
  if session['user_id']:
    return render_template('updateForm.html', user = User.get_one_join_creations({"object_id" : user_id}))
  return redirect('/')

@app.route('/user/update/<int:user_id>', methods=['POST'])
def update_user(user_id):
  data = {
    'first_name': request.form['first_name'],
    'last_name': request.form['last_name'],
    'email': request.form['email'],
    'age': request.form['age'],
    'user_id' : user_id
  }

  User.update_one(data)
  return redirect('/home')