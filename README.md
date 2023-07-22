

# YourFood Backend

![GitHub repo size](https://img.shields.io/github/repo-size/shalugupta5/Food_Application_Backend)
![GitHub last commit](https://img.shields.io/github/last-commit/shalugupta5/Food_Application_Backend)

## Introduction

This is the backend component of YourFood, an innovative online food application that caters to all your culinary cravings. The backend is built using Python and Flask, offering reliable and efficient handling of user orders and interactions.

## Technologies Used

- **Python**: The backend is primarily developed using the Python programming language, known for its simplicity and versatility.
- **Flask**: Flask is used as the web framework for building the backend API. Its lightweight nature and simplicity make it ideal for this project.
- **SQLAlchemy**: SQLAlchemy is utilized as the Object-Relational Mapping (ORM) tool for interacting with the database and handling data operations.
- **Flask-Migrate**: Flask-Migrate provides database migration capabilities, allowing for seamless database schema changes during the development process.
- **Flask-Login**: Flask-Login is used for user authentication, enabling secure and straightforward login functionality.
- **Flask-CORS**: CORS (Cross-Origin Resource Sharing) is integrated to handle cross-origin requests and enable frontend-backend communication.
- **Flask-SocketIO**: Flask-SocketIO is used to implement real-time features, such as order status updates and chat functionalities.
- **SMTP**: For email functionality, SMTP (Simple Mail Transfer Protocol) is utilized to send OTP (One-Time Password) for verification purposes.

## Setup

To set up the backend of YourFood on your local machine, follow these steps:

1. Clone this repository to your local machine.
2. Make sure you have Python and pip installed.
3. Install the required dependencies by running: `pip install -r requirements.txt`.
4. Configure the database connection in the `app.py` file by modifying the `SQLALCHEMY_DATABASE_URI` variable with your database details.
5. Set the SMTP server details in the `app.py` file for email functionality.
6. Run the backend server using the command: `python app.py`.
7. The backend server should now be up and running on `http://localhost:5000`.

## API Endpoints

### Users

- `GET /api/users`: Get all users.
- `GET /api/users/<username>`: Get a specific user by their username.
- `POST /api/users`: Create a new user.
- `DELETE /api/users/<int:user_id>`: Delete a user by their ID.
- `PUT /api/users/<int:user_id>`: Update a user's information.

### Dishes

- `GET /api/dishes`: Get all dishes.
- `POST /api/dishes`: Create a new dish.
- `DELETE /api/dishes/<int:dish_id>`: Delete a dish by its ID.
- `PUT /api/dishes/<int:dish_id>`: Update a dish's information.

### Orders

- `GET /api/orders`: Get all orders.
- `GET /api/orders/<int:order_id>`: Get a specific order by its ID.
- `GET /api/orders/<username>`: Get all orders placed by a specific user.
- `POST /api/orders`: Create a new order.
- `DELETE /api/orders/<int:order_id>`: Delete an order by its ID.
- `PUT /api/orders/<int:order_id>`: Update an order's information.
- `PUT /api/orders/<int:order_id>/tracking`: Update the tracking status of an order.

### Authentication

- `POST /auth/login`: User login with username and password.
- `POST /auth/logout`: User logout.

Please note that some API endpoints might require authentication, and only administrators can access certain routes.

---

**Thank you for exploring the backend of YourFood. This API serves as the backbone for the seamless and delightful dining experience we provide to our users.**

---

## Contact

If you have any questions, feedback, or need support related to the backend of YourFood, feel free to contact us:

- **Email**: For technical inquiries or support, you can reach us at yourfood743@gmail.com 📧

- **LinkedIn**: Connect with us on LinkedIn to stay updated on the latest news and announcements. [Your LinkedIn Profile](https://www.linkedin.com/in/km-shalu-gupta-110207247/) 🔗

We look forward to hearing from you and improving YourFood's backend to provide an even better user experience. Happy coding! 🍕🍔
