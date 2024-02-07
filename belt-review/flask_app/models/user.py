from flask_app.config.mysqlconnection import connect
from flask import flash
from flask_app.models import post
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
  db = 'flaskdecwall'
  def __init__(self, data):
    self.id = data['id']
    self.first_name = data['first_name']
    self.last_name = data['last_name']
    self.email = data['email']
    self.age = data['age']
    self.password = data['password']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    self.posts = []
    
  @classmethod
  def get_one_join_posts(cls, data):
    query ="""
    SELECT * 
    FROM users 
    JOIN posts 
    ON users.id = posts.creator_id 
    WHERE users.id = %(object_id)s
    """
    results = connect(cls.db).query_db(query, data)
    print(results)
    this_user = cls(results[0])
    print(this_user)
    for post_dict in results:
      # create post objects
      post_data = {
        'id' : post_dict['posts.id'],
        'post_content' : post_dict['post_content'],
        'creator_id' : post_dict['creator_id'],
        'created_at' : post_dict['posts.created_at'],
        'updated_at' : post_dict['posts.updated_at'],
      }
      this_post = post.Post(post_data)
      print(this_post)
      # add them to user attribute 'posts'
      this_user.posts.append(this_post)
    # return user object
    print(this_user.posts)
    return this_user

  @classmethod
  def get_by_email(cls, data):
    query = """
    SELECT * 
    FROM users 
    WHERE email = %(user_email)s;"""
    result = connect(cls.db).query_db(query,data)
    # print(result)
    # Didn't find a matching user
    if len(result) < 1:
      return False
    return cls(result[0])

  @classmethod
  def create_one(cls, data):
    query = """
    INSERT INTO users 
    (first_name, last_name, email, password, age)
    VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, %(age)s);
    """
    user_id = connect(cls.db).query_db(query,data)
    print(f"returned user id from query: {user_id}")
    return user_id

  @staticmethod
  def validate(request):
    is_valid = True
    # print(request['first_name'])
    # print(type(request['first_name']))
    if not request['first_name'].strip():
      is_valid = False
      flash("First Name Required", "reg")
    elif len(request['first_name']) < 3:
      is_valid = False
      flash("First Name Must Be Longer", "reg")
    if not request['last_name'].strip():
      is_valid = False
      flash("Last Name Required", "reg")
    elif len(request['last_name']) < 3:
      is_valid = False
      flash("Last Name Must Be Longer", "reg")
    if not request['age'].strip():
      is_valid = False
      flash("Age Required", "reg")
    elif int(request['age']) < 18:
      is_valid = False
      flash("Must Be 18", "reg")
    if not request['email'].strip():
      is_valid = False
      flash("Email Required", "reg")
    elif not EMAIL_REGEX.match(request['email']): 
      is_valid = False
      flash("Invalid email address!", "reg")
    # check for unique email
    if User.get_by_email({'user_email':request['email']}):
      is_valid = False
      flash("Choose another email address!", "reg")
    if not request['password'].strip():
      is_valid = False
      flash("Password Required", "reg")
    elif len(request['password']) < 8:
      is_valid = False
      flash("Password Must Be 8 Characters", "reg")
    elif not request['password'] == request['password_conf']:
      is_valid = False
      flash("Passwords Must Match", "reg")
    return is_valid

  @classmethod
  def get_one(cls, data):
    query ="""
    SELECT * FROM users
    WHERE id = %(object_id)s
    """
    result = connect(cls.db).query_db(query, data)
    return cls(result[0])

  @classmethod
  def get_all(cls):
    query ="""
    SELECT * 
    FROM users;
    """
    result = connect(cls.db).query_db(query)
    output = []
    for dictionary in result:
      this_user = cls(dictionary)
      output.append(this_user)
    return output


  # @classmethod
  # def get_one_join_creations(cls, data):
  #   query ="""
  #   SELECT * 
  #   FROM users
  #   LEFT JOIN cars
  #   ON users.id = cars.creator_id
  #   WHERE users.id = %(object_id)s
  #   """
  #   result = connect(cls.db).query_db(query,data)
  #   print(f"result: {result}")
  #   this_user = cls(result[0])
  #   # print(this_user)
  #   for car_dict in result:
  #     # print(car_dict)
  #     car_data = {
  #       "id" : car_dict['cars.id'],
  #       "make" : car_dict['make'],
  #       "model" : car_dict['model'],
  #       "year" : car_dict['year'],
  #       "color" : car_dict['color'],
  #       "creator_id" : car_dict['creator_id'],
  #       "created_at" : car_dict['cars.created_at'],
  #       "updated_at" : car_dict['cars.updated_at'],
  #     }
  #     this_user.all_cars.append(car.Car(car_data))
  #   # print(this_user.all_cars)
  #   return this_user



  # @classmethod
  # def delete_one(cls, user_id):
  #   data = {"object_id":user_id}
  #   query ="""
  #   DELETE FROM users
  #   WHERE id = %(object_id)s
  #   """
  #   connect(cls.db).query_db(query, data)
  
  # @classmethod
  # def update_one(cls, data):
  #   query ="""
  #   UPDATE users 
  #   SET 
  #   first_name = %(first_name)s,
  #   last_name = %(last_name)s,
  #   email = %(email)s,
  #   age = %(age)s
  #   WHERE id = %(user_id)s
  #   """
  #   connect(cls.db).query_db(query, data)

