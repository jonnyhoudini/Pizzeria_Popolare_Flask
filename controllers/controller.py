from flask import render_template
from app import app
from models.order_list import pizzas

@app.route('/orders')
def index():
    return render_template('index.html', title="Order Management at Pizzeria Popolare", pizzas=pizzas)

@app.route('/orders/<index>')
def get_order(index):
    chosen_order = pizzas[int(index)]
    return render_template('order.html', order=chosen_order)
