
# _ OOP Pt2
# < Starting off with lecture code from yesterday
# done todo Refactor User class to recieve a dictionary as an argument
# todo Add a method to loop through pretend DB and create user objects
# ~   import pretend DB
# todo Refactor methods for @staticmethod & @classmethod where applicable
# . @classmethod & @saticmethod
# . decorators offer us the opportunity to organize our code in a better way
# . Functionality differences are minimal
# < @classmethod
# ~   Instead of implicitly passing `self` into the method, we pass `cls`. 
# ~      This is reference to the class constructor.
# ~   Thus: class methods have no access to the instance (or any attribute that starts with self)
# < @staticmethod
# ~   no access to instance or class attributes
# ~   Thus:  if we need any pre-existing values, they need to be passed in as arguments
# todo Refactor display method to either 
# ~   display all 
# ~   display one
# ~   utilize static helper method
# todo Associate a Post class
# ~   create method to create a post for a specific user
# ~   utiliize static helper method from display method

# from dir import file
from pretendDBresponse import people
# print(people)
from post import Post

class User:
	# Class Attributes/Properties/DATA
	species = "homo sapiens"
	all_users = []
	def __init__(self, users_info_dict): # Constructor Method
    # Instance Properties/Attributes/DATA
    # attributes to refrence dictionary key value pairs not parameters -> positional arguments
		self.id = users_info_dict["id"]
		self.first_name = users_info_dict["first_name"]
		self.last_name = users_info_dict["last_name"]
		self.age = users_info_dict["age"]
		self.email = users_info_dict["email"]
		self.has_kids = users_info_dict["has_kids"]
		self.children = users_info_dict["children"]
		self.posts = []
		User.all_users.append(self)
	
	# Methods/functions/ACTIONS
	def have_birthday(self):
		self.age += 1
		return self
	
	def greeting(self, new_friend):
		print(f"Hello {new_friend.first_name}, I'm {self.first_name}")
		return self
	
	def have_children(self, child):
		# f"user name: {self.first_name}"
		self.children.append(child)
		return self
	
	# Without __repr__ this would print <__main__.User object at 0x000002EEAE0A3AF0>
	def __repr__(self):
		return f"""User: (
		ID: {self.id},
		First Name: {self.first_name},
		Last Name: {self.last_name},
		Age: {self.age},
		Email: {self.email},
		Has_kids: {self.has_kids},
		Children: {self.children},
		Posts: {self.posts},
		)"""
	
	@classmethod
	def display_all_users(cls, user_to_find_id = False):
		print(f"{len(cls.all_users)} users added")
		# print(User.all_users)
		# print(cls.first_name)
		for curent_user in cls.all_users:
			# if current user.id == user_to_find_id
			print(curent_user.id)
			print(curent_user.first_name)
			if user_to_find_id:
				if cls.found_user(curent_user, user_to_find_id):
					print(curent_user)
					return
					# print only that user info
				# else display all of em
			else:
				print(curent_user)
	
	@classmethod
	def create_users(cls):
    # loop through people list and send each person dict to the constructor
		for each_dict in people:
			# print(each_dict)
			cls(each_dict)
	
	@classmethod
	def create_post(cls, poster_id, post_content):
		# loop though users
		for poster in cls.all_users:
			# find the user by id who is posting
			if cls.found_user(poster, poster_id):
				# add that post to list of posts attribute
				poster.posts.append(Post(post_content))
	
	@staticmethod
	def found_user(current_user, id_to_find):
		if current_user.id == id_to_find:
			return True
		else:
			return False

user1 = {
        'id': 1,
        'first_name': 'Cameron',
        'last_name': 'Smith',
        'email': 'cs@email.com',
        'age': 34,
        'has_kids': True,
        'children': ['Harper', 'Walter']
    }
# print(user1['first_name'])
user_object = User(user1)
# print(user_object)
User.create_users()
User.create_post(8,"HIIIII")
User.create_post(8,"Patrick")
User.create_post(8,"how are you?")
User.create_post(6,"HIIIII")
User.display_all_users()