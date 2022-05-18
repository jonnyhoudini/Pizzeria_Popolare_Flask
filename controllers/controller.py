from flask import render_template
from app import app
from models.order_list import pizzas

@app.route('/')
def index():
    return "Pizzeria Popolare"

@app.route('/<name>')
def greet(name):
    return f"Benvenuto to the Pizzeria Popolare, {name}!"

@app.route('/orders')
def get_orders():
    return render_template('index.html', pizzas=pizzas)