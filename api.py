

from flask import Blueprint, request, jsonify
from models import db, User, Dish, Orders
import bcrypt
import hashlib
from flask_login import current_user, login_required
from flask_cors import CORS



api_bp = Blueprint('api', __name__)

@api_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    result = [{'id': user.id, 'username': user.username, 'role': user.role} for user in users]
    return jsonify(result)

@api_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')

    if not username or not password or not role:
        return jsonify({'error': 'Invalid data'})

    # Generate the hashed password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Truncate the hashed password if it exceeds the maximum length
    max_password_length = 100  # Modify this according to your column definition
    if len(hashed_password) > max_password_length:
        hashed_password = hashed_password[:max_password_length]

    if role == 'admin':
        token = data.get('token')  # Token field

        if token != 'token':
            return jsonify({'error': 'Invalid token'})

    user = User(username=username, role=role, password=hashed_password)

    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'})



# Delete user
@api_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({'error': 'User not found'})

    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': 'User deleted successfully'})


# Update user
@api_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({'error': 'User not found'})

    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')

    if username:
        user.username = username
    if password:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        max_password_length = 100  # Modify this according to your column definition
        if len(hashed_password) > max_password_length:
            hashed_password = hashed_password[:max_password_length]
        user.password = hashed_password
    if role:
        user.role = role

    db.session.commit()

    return jsonify({'message': 'User updated successfully'})


# Similar routes and functions can be implemented for dishes and orders
# Example routes for dishes

@api_bp.route('/dishes', methods=['GET'])
def get_dishes():
    dishes = Dish.query.all()
    result = [{'id': dish.id, 'name': dish.name, 'price': dish.price, 'quantity':dish.quantity,'availability': dish.availability} for dish in dishes]
    return jsonify(result)

@api_bp.route('/dishes', methods=['POST'])

def create_dish():
    # if current_user.role != 'admin':
    #     return jsonify({'error': 'Unauthorized access'})
    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    quantity = data.get('quantity')
    availability = data.get('availability')

    if not name or not price or not availability:
        return jsonify({'error': 'Invalid data'})

    dish = Dish(name=name, price=price, quantity=quantity, availability=availability)

    db.session.add(dish)
    db.session.commit()

    return jsonify({'message': 'Dish created successfully'})



# Delete dish
@api_bp.route('/dishes/<int:dish_id>', methods=['DELETE'])

def delete_dish(dish_id):
    # if current_user.role != 'admin':
    #     return jsonify({'error': 'Unauthorized access'})
    dish = Dish.query.get(dish_id)

    if not dish:
        return jsonify({'error': 'Dish not found'})

    db.session.delete(dish)
    db.session.commit()

    return jsonify({'message': 'Dish deleted successfully'})


# Update dish
@api_bp.route('/dishes/<int:dish_id>', methods=['PUT'])

def update_dish(dish_id):
    # if current_user.role != 'admin':
    #     return jsonify({'error': 'Unauthorized access'})
    dish = Dish.query.get(dish_id)

    if not dish:
        return jsonify({'error': 'Dish not found'})

    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    quantity = data.get('quantity')
    availability = data.get('availability')

    if name:
        dish.name = name
    if price:
        dish.price = price
    if availability is not None:  # Check for None explicitly
        dish.availability = bool(availability)

    db.session.commit()

    return jsonify({'message': 'Dish updated successfully'})

# Example routes for orders

@api_bp.route('/orders', methods=['GET'])
# @login_required
def get_orders():
    # if current_user.role != 'admin':
    #     return jsonify({'error': 'Unauthorized access'})
    orders = Orders.query.all()
    result = [{'id': orde.id, 'customer_name': orde.customer_name, 'total_price': orde.total_price, 'status': orde.status} for orde in orders]
    return jsonify(result)

@api_bp.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    customer_name = data.get('customer_name')
    total_price = data.get('total_price')
    status = data.get('status')

    if not customer_name or not total_price or not status:
        return jsonify({'error': 'Invalid data'})

    orders = Orders(customer_name=customer_name, total_price=total_price, status=status)

    db.session.add(orders)
    db.session.commit()

    return jsonify({'message': 'Order created successfully'})


# Delete order
@api_bp.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    orders = Orders.query.get(order_id)

    if not orders:
        return jsonify({'error': 'Order not found'})

    db.session.delete(orders)
    db.session.commit()

    return jsonify({'message': 'Order deleted successfully'})


# Update order
@api_bp.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    orders = Orders.query.get(order_id)

    if not orders:
        return jsonify({'error': 'Order not found'})

    data = request.get_json()
    customer_name = data.get('customer_name')
    total_price = data.get('total_price')
    status = data.get('status')

    if customer_name:
        orders.customer_name = customer_name
    if total_price:
        orders.total_price = total_price
    if status:
        orders.status = status

    db.session.commit()

    return jsonify({'message': 'Order updated successfully'})
