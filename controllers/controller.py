from flask import render_template
from app import app
from models.order_list import pizzas

@app.route('/')
def index():
    return render_template('index.html', pizzas=pizzas)

@app.route('/orders/<index>')
def get_order(index):
    return return render_template('order.html', pizzas=pizzas)
