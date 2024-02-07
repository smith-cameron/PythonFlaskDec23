from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.message import Message


# ? limit all_users to all but current user
# @app.route('/message/new')
# def message_new():
#   return render_template('display.html',
#   current_user = User.get_one_join_posts({'object_id': session['user_id']}),
#   all_users = User.get_all(),
#   my_messages = Message.get_all_join_sender_by_reciever_id({'reciever_id':session['user_id']}))

@app.route('/message/create', methods=['post'])
def message_create():
  print(request.form)
  # validate message form
  if Message.validate(request.form):
    # if valid add sender id
    data = request.form.to_dict()
    data['sender_id'] = session['user_id']
    Message.create_one(data)
    # create message object
  # else redirect for form and display errors
  return redirect(f'/user/display/{session["user_id"]}')