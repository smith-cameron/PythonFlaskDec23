from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.post import Post

@app.route('/post/edit/<int:post_id>')
def edit_post(post_id):
  if session['user_id']:
    this_post = Post.get_one({'object_id': post_id})
    if this_post.creator.id == session['user_id']:
      # load html with for to edit post
      return render_template('edit.html',post_to_edit = this_post)
    return redirect('/user/home')
  return redirect('/')

@app.route('/post/update/<int:post_id>', methods=['POST'])
def update_post(post_id):
  print(request.form)
  if Post.validate(request.form):
    print("its valid")
    # Call the update method for Post
    data = request.form.to_dict()
    data['object_id'] = post_id
    Post.update_one(data)
    return redirect('/user/home')
  return redirect(f'/post/edit/{post_id}')

@app.route('/post/create', methods=['POST'])
def publish_post():
  print(request.form)
  if Post.validate(request.form):
    print("its valid")
    #, need to add creator_id from session to the request.form
    # data = {
    #   'post_content': request.form['post_content'],
    #   'creator_id': session['user_id']
    # }
    data = request.form.to_dict()
    # print(type(data))
    data['creator_id'] = session['user_id']
    # print(data)
    # Call the create method for Post
    Post.create_one(data)
    return redirect('/user/home')
  return redirect('/user/home')

@app.route("/post/delete/<int:post_id>")
def delete_post(post_id):
  if session['user_id']:
    data = {'object_id':post_id}
    # check that the logged in user is in fact the creator of the object to be deleted
    # Post.get_one({'object_id':post_id})
    if session['user_id'] == Post.get_one(data).creator.id:
      # print('you are the correct person')
      Post.delete_one(data)
    return redirect('/user/home')
  return redirect('/')