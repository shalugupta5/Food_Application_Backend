import pytest
from app import app, db
from models import User, Dish, Orders


@pytest.fixture(scope='session')
def client():
    app.config['TESTING'] = True
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()



# def test_create_user(client):
#     data = {
#         'username': 'testuser',
#         'password': 'testpassword',
#         'role': 'admin',
#         'wallet': 100.0
#     }
#     response = client.post('/api/users', json=data)
#     assert response.status_code == 200
#     assert response.json == {'message': 'User created successfully'}

#     # Check if the user is created in the database
#     user = User.query.filter_by(username='testuser').first()
#     assert user is not None
#     assert user.role == 'admin'
#     assert user.wallet == 100.0


# def test_get_users(client):
#     # Create a test user
#     test_user = User(username='testuser', password='testpassword', role='admin')
#     db.session.add(test_user)
#     db.session.commit()

#     response = client.get('/api/users')
#     assert response.status_code == 200
#     assert isinstance(response.json, list)
#     assert len(response.json) == 1
#     assert response.json[0]['username'] == 'testuser'


# # Add tests for other API routes (get_user_by_username, delete_user, update_user, etc.)

# def test_create_dish(client):
#     data = {
#         'name': 'Test Dish',
#         'price': 10.0,
#         'quantity': 5,
#         'availability': True
#     }
#     response = client.post('/api/dishes', json=data)
#     assert response.status_code == 200
#     assert response.json == {'message': 'Dish created successfully'}

#     # Check if the dish is created in the database
#     dish = Dish.query.filter_by(name='Test Dish').first()
#     assert dish is not None
#     assert dish.price == 10.0
#     assert dish.quantity == 5
#     assert dish.availability == True


# def test_get_dishes(client):
#     # Create a test dish
#     test_dish = Dish(name='Test Dish', price=10.0, quantity=5, availability=True)
#     db.session.add(test_dish)
#     db.session.commit()

#     response = client.get('/api/dishes')
#     assert response.status_code == 200
#     assert isinstance(response.json, list)
#     assert len(response.json) == 1
#     assert response.json[0]['name'] == 'Test Dish'


# # Add tests for other API routes related to dishes (delete_dish, update_dish, etc.)

# def test_create_order(client):
#     data = {
#         'customer_name': 'Test Customer',
#         'total_price': 50.0,
#         'status': 'pending',
#         'tracking_status': 'in progress'
#     }
#     response = client.post('/api/orders', json=data)
#     assert response.status_code == 200
#     assert response.json == {'message': 'Order created successfully'}

#     # Check if the order is created in the database
#     order = Orders.query.filter_by(customer_name='Test Customer').first()
#     assert order is not None
#     assert order.total_price == 50.0
#     assert order.status == 'pending'
#     assert order.tracking_status == 'in progress'


# def test_get_orders(client):
#     # Create a test order
#     test_order = Orders(customer_name='Test Customer', total_price=50.0, status='pending', tracking_status='in progress')
#     db.session.add(test_order)
#     db.session.commit()

#     response = client.get('/api/orders')
#     assert response.status_code == 200
#     assert isinstance(response.json, list)
#     assert len(response.json) == 1
#     assert response.json[0]['customer_name'] == 'Test Customer'


# # Add tests for other API routes related to orders (get_order, delete_order, update_order, etc.)

