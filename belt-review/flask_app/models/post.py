from flask_app.config.mysqlconnection import connect
from flask import flash
from flask_app.models import user

class Post:
  db = 'flaskdecwall'
  def __init__(self, data):
    self.id = data['id']
    self.post_content = data['post_content']
    self.creator_id = data['creator_id']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    self.creator = None

  @classmethod
  def update_one(cls, data):
    query ="""
    UPDATE posts SET post_content = %(post_content)s
    WHERE id = %(object_id)s
    """
    connect(cls.db).query_db(query, data)

  @classmethod
  def delete_one(cls, data):
    query ="""
    DELETE FROM posts
    WHERE id = %(object_id)s
    """
    connect(cls.db).query_db(query, data)

  @classmethod
  def get_one(cls, data):
    query ="""
    SELECT * FROM posts
    JOIN users
    ON posts.creator_id = users.id
    WHERE posts.id = %(object_id)s
    """
    result = connect(cls.db).query_db(query, data)
    # print(result)
    this_post = cls(result[0])
    # print(this_post.creator)
    user_data = {
        'id' : result[0]['users.id'],
        'first_name' : result[0]['first_name'],
        'last_name' : result[0]['last_name'],
        'email' : result[0]['email'],
        'age' : None,
        'password' : None,
        'created_at' : result[0]['users.created_at'],
        'updated_at' : result[0]['users.updated_at']
      }
    this_post.creator = user.User(user_data)
    # print(this_post.creator)
    return this_post


  @staticmethod
  def validate(request):
    is_valid = True
    if not request['post_content']:
      is_valid = False
      flash("Post Content Required", "post")
    elif len(request['post_content']) < 10:
      is_valid = False
      flash("Post Content Must Be Longer", "post")
    return is_valid

  @classmethod
  def create_one(cls, data):
    query = """
    INSERT INTO posts 
    (post_content, creator_id)
    VALUES (%(post_content)s, %(creator_id)s);
    """
    post_id = connect(cls.db).query_db(query,data)
    print(f"returned post id from query: {post_id}")
    # return post_id

  @classmethod
  def get_all(cls):
    query="""
    SELECT * 
    FROM posts
    JOIN users
    ON posts.creator_id = users.id;
    """
    results = connect(cls.db).query_db(query)
    # print(results)
    output = []
    for query_dictionary in results:
      # print(query_dictionary)
      # create post objects
      this_post = cls(query_dictionary)
      # print(this_post)
      # create distionary to pass to User constructor
      user_data = {
        'id' : query_dictionary['users.id'],
        'first_name' : query_dictionary['first_name'],
        'last_name' : query_dictionary['last_name'],
        'email' : query_dictionary['email'],
        'age' : query_dictionary['age'],
        'password' : None,
        'created_at' : query_dictionary['users.created_at'],
        'updated_at' : query_dictionary['users.updated_at']
      }
      # create User object
      # set creator attribute to this_post.this_creator User object
      this_post.creator = user.User(user_data)
      # put the post object into the output list
      output.append(this_post)
    print(output)
    return output