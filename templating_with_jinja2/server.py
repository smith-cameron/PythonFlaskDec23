from flask import Flask, render_template
app = Flask(__name__)
# ! HEADER OF SERVER

# < JINJA Links -> https://jinja.palletsprojects.com/en/3.1.x/templates/#template-designer-documentation
# . Filters -> https://jinja.palletsprojects.com/en/3.1.x/templates/#list-of-builtin-filters
# . Tests -> https://jinja.palletsprojects.com/en/3.1.x/templates/#list-of-builtin-tests
#   ? Returns a boolean
# . Math -> https://jinja.palletsprojects.com/en/3.1.x/templates/#math
# . Comparitors and Logic -> https://jinja.palletsprojects.com/en/3.1.x/templates/#comparisons
# . Msc Operators -> https://jinja.palletsprojects.com/en/3.1.x/templates/#other-operators

# . Route Body/Block START
@app.route("/")
def my_root_route_function():
  return """
    {% ... %} for Statements
    {{ ... }} for Expressions to print to the template output
    {# ... #} for Comments not included in the template output
  """
# . Route Body/Block END

# . Route Body/Block START
@app.route("/liftoff/<airport>/<int:countdown>")
def my_other_function(airport,countdown):
  print(countdown)
  return render_template("index.html", 
  unicorn = countdown,
  airport = airport,
  things = ["flying","flying","flying","flying","flying"]
  )
# . Route Body/Block END

# . Route Body/Block START
@app.route("/event/<traffic_controller>/<int:status>")
def method_names_dont_matter(traffic_controller, status):
  # print(type(status))
  # print(bool(status))
  observation = "we have a problem"
  return render_template("index2.html",
  traffic_controller=traffic_controller,
  is_event = bool(status),
  obs = observation
  )
# . Route Body/Block END

# . Route Body/Block START
@app.route("/lists")
def lists():
  student_info = [
    {'name' : 'Gort', 'age' : 35},
    {'name' : 'Ben', 'age' : 30 },
    {'name' : 'Timmy', 'age' : 25},
    {'name' : 'DB', 'age' : 27}
  ]
  return render_template("index2.html", random_numbers = [3,1,5], students = student_info)
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

