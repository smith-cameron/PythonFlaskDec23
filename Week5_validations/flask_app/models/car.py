from flask_app.config.mysqlconnection import connect
from flask_app.models import user
from flask import flash

class Car:
  db = 'flaskdec23'
  def __init__(self, data):
    self.id = data['id']
    self.make = data['make']
    self.model = data['model']
    self.year = data['year']
    self.color = data['color']
    self.creator_id = data['creator_id']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    self.creator = None

  @classmethod
  def delete_one(cls, data):
    query="""
    DELETE FROM cars 
    WHERE id = %(car_id)s
    """
    connect(cls.db).query_db(query,data)

  @staticmethod
  def validate(request):
    print(request)
    is_valid = True

    # <Validation for 'make'
    if not request['make']:
      is_valid = False
      flash("Please provide a vehicle make.", "car")
    elif len(request['make']) < 3:
      is_valid = False
      flash("Please provide a longer word for vehicle make.", "car")

    # <Validation for 'model'
    if not request['model']:
      is_valid = False
      flash("Please provide a vehicle model.", "car")
    elif len(request['model']) < 3:
      is_valid = False
      flash("Please provide a longer word for vehicle model.", "car")

    # <Validation for 'year'
    if not request['year']:
      is_valid = False
      flash("Please provide a vehicle year.", "car")
    elif int(request['year']) <= 1920 or int(request['year']) >= 2025:
      is_valid = False
      flash("Please provide a vehicle year between 1920 and next year.", "car")

    # <Validation for 'color'
    if not request['color']:
      is_valid = False
      flash("Please provide a vehicle color.", "car")
    elif len(request['color']) < 3:
      is_valid = False
      flash("Please provide a valid color.", "car")

    print(is_valid)
    return is_valid

  @classmethod
  def create_one(cls, data):
    query = """
    INSERT INTO cars 
    (make, model, year, color, creator_id)
    VALUES (%(make)s, %(model)s, %(year)s, %(color)s, %(creator_id)s);
    """
    result = connect(cls.db).query_db(query,data)

  @classmethod
  def get_all_join_creator(cls):
    query ="""
      SELECT * 
      FROM cars
      JOIN users
      ON cars.creator_id = users.id;
    """
    result = connect(cls.db).query_db(query)
    # print(result)
    output = []
    for query_dictionary in result:
      # print(car_dictionary)
      # create a car object
      this_car = cls(query_dictionary)
      # initialize dict to refrence and hold user specific columns
      user_data = {
        'id' : query_dictionary['users.id'],
        'first_name' : query_dictionary['first_name'],
        'last_name' : query_dictionary['last_name'],
        'email' : query_dictionary['email'],
        'age' : query_dictionary['age'],
        'password' : query_dictionary['password'],
        'created_at' : query_dictionary['users.created_at'],
        'updated_at' : query_dictionary['users.updated_at']
      }
      # create user object with new dict above
      this_user = user.User(user_data)
      # print(this_user.id)
      # add that user as the car creator
      this_car.creator = this_user
      # append into output list to loop through in the html
      output.append(this_car)
    # print(output)
    return output