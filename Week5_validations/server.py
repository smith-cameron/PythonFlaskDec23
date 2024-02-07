from flask_app import app
from flask import  render_template, redirect
from flask_app.models.user import User
from flask_app.models.car import Car
# . Add controller imports as required
from flask_app.controllers import user_controller, car_controller

#< handle root route access
#* Not required -> Project Specific
@app.route('/')
def index():
    return render_template("index.html")

# ! FOOTER OF SERVER
# < Below every route/function
# < It is ALWAYS the last lines of the file
if __name__ == '__main__':
    app.run(debug=True)