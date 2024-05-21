import datetime
from functools import wraps

from flask import Flask, g, request, jsonify
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import jwt


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

DATABASE = 'database.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT UNIQUE NOT NULL,
                            password TEXT NOT NULL
                          )''')
        db.commit()


init_db()


def is_authenticated(f):
    @wraps(f)  # functools wraps prevents the override of the wrapped function
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'message': 'Token is missing'}), 403

        try:
            jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        except Exception as Ex:
            return jsonify({'message': f'Token is invalid ({Ex})'}), 403

        return f(*args, **kwargs)
    return decorated


@app.route('/signup', methods=['POST'])
def signup():
    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        db.commit()
        return jsonify({'message': 'User registered successfully'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'message': 'Username already exists'}), 409


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()

    if user and check_password_hash(user[2], password):
        token = jwt.encode({'username': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, app.config['SECRET_KEY'])
        return jsonify({'token': token}), 200

    return jsonify({'message': 'Invalid credentials'}), 401


@app.route('/users/<user_id>', methods=['GET'])
@is_authenticated
def users(user_id):
    print(f"USER ID {user_id}")
    if not user_id:
        return jsonify({'message': 'User ID is required'}), 400

    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT id, username FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()

    if user is None:
        return jsonify({'message': 'User not found'}), 404

    return jsonify({'id': user[0], 'username': user[1]}), 200


if __name__ == '__main__':
    app.run(debug=True)
