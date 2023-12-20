from flask import Flask
#, Initialize Flask instance
app = Flask(__name__)
#. Set a secret key for session management
app.secret_key = 'something... really, anything.'