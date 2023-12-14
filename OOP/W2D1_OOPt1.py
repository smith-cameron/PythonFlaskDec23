
# _ OOP
# < A programming paradigm that:
  # . organizes data and behavior into reusable and self-contained objects(CLASSes). 
  # < These class objects contain both 
    # . self.data (attributes or properties) 
      # > AND 
    # . methods() (functions or procedures) 
  # < that operate on the data. 
# ! The primary purpose of OOP is to increase the reusability and maintainability of code

# > Class
  # ~ A class is a blueprint or a template for creating objects. 
  # ~ It defines the properties (attributes) and methods (functions) that the objects of the class will have.
  # ~ Represents what each INSTANCE(object) will look like

# > OBJECT
  # ~ An object is a real-world entity that is an instance of a class. 
  # ~ It represents a unique occurrence of a class.
  # ~ All users have the same structure but my info is different than yours

# todo SYNTAX:
# , starts with the 
  # ! class 
# , keyword followed by
  # ! ClassName (capitalized and singular) and a colon :

class User:
	# Class Attributes/Properties/DATA
	species = "homo sapiens"
	all_users = []
	def __init__(self, f_name, l_name, age, email, has_kids = False): # Constructor Method
    # Instance Properties/Attributes/DATA
		self.first_name = f_name
		self.last_name = l_name
		self.age = age
		self.email = email
		self.has_kids = has_kids
		self.children = []
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
	
	def __repr__(self):
		return f"""User: (
		First Name: {self.first_name},
		Last Name: {self.last_name},
		Age: {self.age},
		Email: {self.email},
		Has_kids: {self.has_kids},
		Children: {self.children},
		)"""
	
	def display_all_users():
		print(f"{len(User.all_users)} users added")
		# print(User.all_users)
		for i in User.all_users:
			# Without __repr__ this would print <__main__.User object at 0x000002EEAE0A3AF0>
			print(i)

user1 = User("Jane", "Doe", 56, "jd@email.com", True)
user2 = User("John", "Doe", 56, "jd@email.com")
user3 = User("Timmy", "Jimmy-Jam", 34, "tjj@email.com")
print(user1)
print(user2.age)
user2.age = 57
user2.age += 1
# user1.children.append(user3)
user1.greeting(user2).have_children(user3).have_birthday()
# user3.have_birthday()
print(user3.age)
User.display_all_users()
print(User.all_users)