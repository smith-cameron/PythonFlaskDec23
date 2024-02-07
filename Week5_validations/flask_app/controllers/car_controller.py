from flask_app import app
from flask import  render_template, redirect, request, session
from flask_app.models.car import Car
import random
user_ids = [1,3,4,5,7,10,14,16]
random_id = random.choice(user_ids)  

@app.route('/car/new')
def car_new():
  return render_template("createCar.html")

@app.route('/car/create', methods=['POST'])
def create_car():
  # < Validate user provided form information
  if Car.validate(request.form):
    #< continue to process and save form data
    data = {
      'make': request.form['make'],
      'model': request.form['model'],
      'year': request.form['year'],
      'color': request.form['color'],
      'creator_id' : session['user_id']
      # after login and reg this will be provided from session['user_id_key']
    }
    Car.create_one(data)
    # <redirect somewhere good
    return redirect('/home')
  # <else redirect to ROUTE RENDERING THE ORIGONAL FORM
  return redirect("/car/new")

# todo delete a car routing/mtehods
@app.route('/car/delete/<int:car_id>')
def delete_car(car_id):
  Car.delete_one({'car_id': car_id})
  return redirect('/home')