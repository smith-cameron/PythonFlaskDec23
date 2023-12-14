from flask import Flask
app = Flask(__name__)
# ! HEADER OF SERVER

# > Route Body/Block START
@app.route("/")
def my_root_route_function():
  return "helloooooooo World"
# > Route Body/Block END

# > Route Body/Block START
@app.route("/")
def my_root_route_function():
  return "helloooooooo World"
# > Route Body/Block END

# > Route Body/Block START
@app.route("/")
def my_root_route_function():
  return "helloooooooo World"
# > Route Body/Block END

# > Route Body/Block START
@app.route("/")
def my_root_route_function():
  return "helloooooooo World"
# > Route Body/Block END

# > Route Body/Block START
@app.route("/")
def my_root_route_function():
  return "helloooooooo World"
# > Route Body/Block END


# ! FOOTER OF SERVER
# < Below every route/function
# < It is ALWAYS the last lines of the file
if __name__ == "__main__":
  app.run(debug=True)