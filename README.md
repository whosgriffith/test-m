# Test Desarrollador Backend

### Como ejecutar las soluciones:

First install requirements.txt
```pip install -r requirements.txt```

#### Sección 1: Python
Run read_file.py
```python read_file.py``` or from root ```python python/read_file.py```

Run decorator.py
```python decorator.py``` or from root ```python python/decorator.py```

#### Sección 2: Flask
Run app.py
```python app.py``` or from root ```python flask_app/app.py```

Endpoints:
- **/signup**
Payload: Multipart form with username and password
- **/users/{id}**
Header: `Authorization` with token from login
- **/login**
Payload: Multipart form with username and password

#### Sección 3: Django
Make migrations
```python manage.py makemigrations```

Migrate
```python manage.py migrate```

Run test server
```python manage.py runserver```

URLS donde se pueden probar las views.

    path('signup/', SignupView.as_view(), name='signup'),
    path('users/', UsersListView.as_view(), name='users_list'),
    path('products/', ListProductsView.as_view(), name='products_list'),
