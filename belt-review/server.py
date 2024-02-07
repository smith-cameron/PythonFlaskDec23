from flask_app import app
from flask_app.controllers import user_controller, post_controller, message_controller
# secret key for session
app.secret_key = "Whatever you want, as long as its a string"

if __name__ == "__main__":
  app.run(debug=True)