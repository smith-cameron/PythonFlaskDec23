from flask import Flask
app = Flask(__name__)
# ! HEADER OF SERVER

# . Route Body/Block START
@app.route("/")
def my_root_route_function():
  return "helloooooooo World"
# . Route Body/Block END

# . Route Body/Block START
@app.route("/liftoff")
def my_other_function():
  return "Houston we have liftoff!!!!!!"
# . Route Body/Block END

# . Route Body/Block START
@app.route("/event")
def method_names_dont_matter():
  return "Houston we have a problem"
# . Route Body/Block END

# . Route Body/Block START
@app.route("/falling")
def they_have_to_be_different():
  return "aaaaaaaaaaaaahhhhhhhhhhh"
# . Route Body/Block END

# . Route Body/Block START
@app.route("/calling")
def and_should_describe():
  return "SOS!"
# . Route Body/Block END

# . Route Body/Block START
@app.route("/landing")
def the_functionality():
  return "BOOM"
# . Route Body/Block END

# ! FOOTER OF SERVER
# < Below every route/function
# < It is ALWAYS the last lines of the file
if __name__ == "__main__":
  app.run(debug=True, port=5500)