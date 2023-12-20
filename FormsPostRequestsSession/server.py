from flask_app import app
from flask_app.controllers import controller
# . Add controllers as required

# ! FOOTER OF SERVER
# < Below every route/function
# < It is ALWAYS the last lines of the file
if __name__ == '__main__':
    app.run(debug=True)