from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify, get_flashed_messages
from flask_app.models.user import User
from flask_app.models.post import Post
from flask_app.models.message import Message
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
  #? init session here? to survive the async fetch()
  return render_template('index.html')

#done TODO DELETE a post
#done TODO Display a single user page(GET route)
  #done todo Show single user and all their posts(using JOIN query)
  #done todo EDIT a post
# TODO Add ability to like a post
# todo Send direct messages
# todo Display all messages recieved
#? Save user input if validation passes on registration
#? Add comment feature to individual posts(dashboard)

@app.route('/user/display/<int:user_id>')
def display(user_id):
  if session['user_id']:
    return render_template('display.html',
      # current_user = User.get_one({'object_id':user_id}),
      current_user = User.get_one_join_posts({'object_id': user_id}),
      all_users = User.get_all(),
      my_messages = Message.get_all_join_sender_by_reciever_id({'reciever_id' : user_id}))
  return redirect('/')

@app.route('/user/home/<int:user_id>')
def dashboard(user_id):
  session['user_id'] = user_id
  if session['user_id']:
    # Add a get all to display all posts
    return render_template("dashboard.html",
    current_user = User.get_one({'object_id':session['user_id']}),
    all_posts = Post.get_all()
    )
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
    # session['user_id'] = user_id
    return jsonify({'success': True, "user_id": user_id})
  errors = {'success': False, 'reg_errors':get_flashed_messages(category_filter = ['reg'])}
  print(f'python errors - {errors}')
  return jsonify(errors)

# todo login routing/method
@app.route('/user/login', methods=['POST'])
def login_user():
  user_in_db = User.get_by_email({'user_email': request.form['email'].strip()})
  if user_in_db:
    if bcrypt.check_password_hash(user_in_db.password, request.form['password']):
      session['user_id'] = user_in_db.id
      return redirect('/user/home')
  flash("Invalid Credentials", "login")
  return redirect('/')