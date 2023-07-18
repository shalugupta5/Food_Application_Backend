


from flask import Blueprint, request, jsonify
from models import db, User, Dish, Orders
import bcrypt
import hashlib
from flask_login import current_user, login_required
from flask_cors import CORS
from flask import session


api_bp = Blueprint('api', __name__)





@api_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    result = [{'id': user.id, 'username': user.username, 'role': user.role, 'wallet':user.wallet} for user in users]
    return jsonify(result)




@api_bp.route('/users/<username>', methods=['GET'])
def get_user_by_username(username):
    user = User.query.filter_by(username=username).first()
    
    if not user:
        return jsonify({'error': 'User not found'})

    user_data = {
        'id': user.id,
        'username': user.username,
        'role': user.role,
        'wallet': user.wallet
    }

    return jsonify(user_data)






@api_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')
    wallet = data.get('wallet')

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
    wallet = data.get('wallet')

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
        
    if wallet:
        user.wallet=wallet

    db.session.commit()

    return jsonify({'message': 'User updated successfully'})




@api_bp.route('/users/<username>', methods=['PUT'])
def update_user_wallet(username):
    user = User.query.filter_by(username=username).first()

    if not user:
        return jsonify({'error': 'User not found'})

    data = request.get_json()
    wallet_balance = data.get('wallet')

    if wallet_balance is not None:
        user.wallet = wallet_balance

    db.session.commit()

    return jsonify({'message': 'User wallet balance updated successfully', 'wallet':user.wallet})



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
    if quantity:
        dish.quantity = quantity
    if availability is not None:  # Check for None explicitly
        dish.availability = bool(availability)

    db.session.commit()

    return jsonify({'message': 'Dish updated successfully','quantity':quantity})

# Example routes for orders

@api_bp.route('/orders', methods=['GET'])
# @login_required
def get_orders():
    # if current_user.role != 'admin':
    #     return jsonify({'error': 'Unauthorized access'})
    orders = Orders.query.all()
    result = [{'id': orde.id, 'customer_name': orde.customer_name, 'dish_name':orde.dish_name, 'total_price': orde.total_price, 'status': orde.status,
    'tracking_status':orde.tracking_status} for orde in orders]
    return jsonify(result)


@api_bp.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    orde = Orders.query.get(order_id)
    if not orde:
        return jsonify({'error': 'Order not found'})
    result = {'id': orde.id, 'customer_name': orde.customer_name, 'dish_name':orde.dish_name, 'total_price': orde.total_price, 'status': orde.status,
              'tracking_status': orde.tracking_status}
    return jsonify(result)



@api_bp.route('/orders/<username>', methods=['GET'])
def get_orders_by_username(username):
    orders = Orders.query.filter_by(customer_name=username).all()

    if not orders:
        return jsonify({'error': 'No orders found for the specified username'})

    result = [{'id': order.id, 'customer_name': order.customer_name, 'dish_name':order.dish_name, 'total_price': order.total_price, 'status': order.status, 'tracking_status': order.tracking_status} for order in orders]
    return jsonify(result)





@api_bp.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    customer_name = data.get('customer_name')
    dish_name = data.get('dish_name')
    total_price = data.get('total_price')
    status = data.get('status')
    tracking_status=data.get('tracking_status')

    if not customer_name or not total_price or not status:
        return jsonify({'error': 'Invalid data'})

    orders = Orders(customer_name=customer_name, dish_name=dish_name, total_price=total_price, status=status, tracking_status=tracking_status)

    db.session.add(orders)
    db.session.commit()

    return jsonify({'message': 'Order created successfully','id':orders.id })


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
    dish_name = data.get('dish_name')
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


@api_bp.route('/orders/<int:order_id>/tracking', methods=['PUT'])
def update_order_tracking(order_id):
    orders = Orders.query.get(order_id)

    if not orders:
        return jsonify({'error': 'Order not found'})

    data = request.get_json()
    tracking_status = data.get('tracking_status')

    if not tracking_status:
        return jsonify({'error': 'Invalid data'})

    orders.tracking_status = tracking_status
    db.session.commit()

    return jsonify({'message': 'Order tracking status updated successfully'})


@api_bp.route('/wallet/balance/<username>', methods=['GET'])
def get_wallet_balance(username):
    user = User.query.filter_by(username=username).first()

    if not user:
        return jsonify({'error': 'User not found'})

    return jsonify({'balance': user.wallet})

