from flask_app.config.mysqlconnection import connect
from flask import flash
from flask_app.models import user

class Message:
  db = 'flaskdecwall'
  def __init__(self, data):
    self.id = data['id']
    self.message_content = data['message_content']
    self.sender_id = data['sender_id']
    self.reciever_id = data['reciever_id']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    self.creator = None
    self.sender = None

  @classmethod
  def create_one(cls, data):
    query = """
    INSERT INTO messages 
    (message_content, reciever_id, sender_id)
    VALUES (%(message_content)s, %(reciever_id)s, %(sender_id)s);
    """
    message_id = connect(cls.db).query_db(query,data)
    print(f"returned message id from query: {message_id}")

  @staticmethod
  def validate(request):
    is_valid = True
    if not request['message_content'].strip():
      is_valid = False
      flash("Message Content Required", "message")
    return is_valid

  @classmethod
  def get_all_join_sender_by_reciever_id(cls, data):
    query=''' 
    SELECT * 
    FROM messages
    JOIN users
    ON messages.sender_id = users.id
    WHERE messages.reciever_id = %(reciever_id)s'''
    results = connect(cls.db).query_db(query,data)
    print(results)
    all_messages = []
    for i in results:
      this_message = cls(i)
      print(this_message)
      user_data = {
        'id' : i['users.id'],
        'first_name' : i['first_name'],
        'last_name' : i['last_name'],
        'email' : i['email'],
        'age' : None,
        'password' : None,
        'created_at' : i['users.created_at'],
        'updated_at' : i['users.updated_at']
      }
      sender_object = user.User(user_data)
      this_message.sender = sender_object
      all_messages.append(this_message)
    return all_messages