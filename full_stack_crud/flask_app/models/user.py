from flask_app.config.mysqlconnection import connect

class User:
  db = 'flaskdec23'
  def __init__(self, data):
    self.id = data['id']
    self.first_name = data['first_name']
    self.last_name = data['last_name']
    self.email = data['email']
    self.age = data['age']
    self.password = data['password']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

  # create() is a classmethod that recieves 
  # arguement of infered cls and data dictionary from controller
  @classmethod
  def create(cls, data_dict):
    # define our query
    # as a multiline string
    query = """
    INSERT INTO users 
    (first_name, last_name, email, password, age)
    VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, %(age)s);
    """
    # send that to our database in a query
    result = connect(cls.db).query_db(query,data_dict)
    print(f"user id: {result}")

  @classmethod
  def get_all(cls):
    query ="""SELECT * 
    FROM users;"""
    result = connect(cls.db).query_db(query)
    print(result)
    # create output list
    output = []
    # iterate through list
    for dictionary in result:
      # access each dictionary
      print(dictionary)
      # turn each dictionary into a class instance
      this_user = cls(dictionary)
      print(this_user)
      # put those instances back in a list
      output.append(this_user)
    print(f"output from model {output}")
    return output

  @classmethod
  def delete_one(cls, data):
    print(data)
    query ="""
    DELETE FROM users
    WHERE id = %(object_id)s
    """
    connect(cls.db).query_db(query, data)
    # No need to return anything

  @classmethod
  def get_one(cls, data):
    print(data)
    query ="""
    SELECT * FROM users
    WHERE id = %(object_id)s
    """
    result = connect(cls.db).query_db(query, data)
    print(result)
    # we should only have one dictionary in the list returned
    # since the first thing lives at index 0 
    # we can pass that to the constructor for this class in our return
    return cls(result[0])

  
  @classmethod
  def update_one(cls, data):
    print(data)
    query ="""
    UPDATE users 
    SET 
    first_name = %(first_name)s,
    last_name = %(last_name)s,
    email = %(email)s,
    age = %(age)s
    WHERE id = %(user_id)s
    """
    connect(cls.db).query_db(query, data)
    # No need to return anything
