
# _ Dictionaries
# < An unordered collection of key-value pairs . 
""" bounded by {}
    keys are typically strings
    colon separated keys : values 
    comma separated pairs
"""
  # > {"key":value, "key":value, ...}
# < Not sequential in memory (NO INDEX)
# < Each KEY in a dictionary is unique
# < Mutable so can shrink or grow or be updated
# < METHODS
  # > https://docs.python.org/3/library/stdtypes.html#typesmapping

# < Create Read Update Delete
# > Create
def create_dict():
  user = {}
  user1 = {
    "first_name" : "Jaida", 
    "last_name" : "Doe",
    "age" : 745,
    "has_kids" : True,
    'children' : ["bert", "ernie"]
    }
  # print(user1)
  return user1
this_user = create_dict()

# > Read
def read_dict_values(input_dict):
  print(input_dict['first_name'])
  print(input_dict.get('last_name'))
  print(input_dict.get('socialSecNum'))
  if "socialSecNum" in input_dict:
    print(input_dict["socialSecNum"])
  else:
    print("Not There")

  if "age" in input_dict:
    print(input_dict["age"])
  else:
    print("Not There")

# read_dict_values(this_user)

# > Update
def update_dict(this_user):
  # var_name = value
  this_user['first_name'] = "John"

  this_user.update({
    "first_name" : "Jane", 
    "last_name" : "Doe",
    "age" : 45,
    "email" : "jd@email.com",
    "has_kids" : True,
    'children' : ["bert", "ernie"]
  })
  # print(this_user)
  return this_user

new_user = update_dict(this_user)

# > Delete
def remove_values(input):
  # print(input)
  del input['email']
  print(input)
# remove_values(new_user)

# < Dictionaries and Loops
# > By Key
def by_key(new_user):
  for iterator in new_user:
    print(iterator)
# by_key(new_user)

# > By Value Via Key
def value_by_key(new_user):
  # dictionary_name['key']
  for iterator in new_user:
    print(f"key: {iterator}")
    print(f"value: {new_user[iterator]}")
# value_by_key(new_user)

# > .keys()
def keys_built_in(new_user):
  for pizza in new_user.keys():
    print(pizza)
# keys_built_in(new_user)

# > .values()
def values_built_in(new_user):
  for value in new_user.values():
    print(value)
# values_built_in(new_user)

# > .items()
def items_built_in(new_user):
  print(new_user.items())
  for unicorn, burning  in new_user.items():
    print(burning)
    print(unicorn)
# items_built_in(new_user)

#  < Practice
# ? Create a function that creates a user dictionary...
all_users = [new_user]
def create_user(f_name, l_name, age, email, has_kids = False):
  user = {
    "first_name" : f_name, 
    "last_name" : l_name,
    "age" : age,
    "email" : email,
    "has_kids" : has_kids,
    'children' : []
  }
  # print(user)
  all_users.append(user)
  return user

user_timmy = create_user("Timmy", "Jimmy-Jam", 33, "tjj@email.com")
create_user("Ben", "Jammin", 43, "bj@email.com")
create_user("Clint", "Eastwood", 399, "ce@email.com", True)
create_user("DB", "Cooper", 90, "db@email.com")
create_user("Kaya", "Seawalker", 26, "ks@email.com")

# ? Add each dictionary to a list
# ? Create a function that searches for a user and update children
def find_one(all_users, user_name, kid_to_add):
  # print(f"all_users: {all_users}\n")
  # loop through all the users
  for user in all_users:
    # print(user)
    # find one user by name
    # print(user["first_name"])
    # conditional (is this the one?)
    if user["first_name"] == user_name:
      # print(f"found ya {user_name}")
      user['children'].append(kid_to_add)
      user['has_kids'] = True

find_one(all_users,"Timmy", this_user)
new_user['children'].append(user_timmy)

find_one(all_users,"DB", "Zebulon")
find_one(all_users,"Clint", [this_user, "Sam"])
print(all_users)
