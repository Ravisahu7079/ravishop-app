import pytest
from app import create_app, db

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test__health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert data['app'] == 'RaviShop'

def test_get_products_empty(client):
    response = client.get('/products')
    assert response.status_code == 200
    assert response.get_json() == []

def test_create_product(client):
    response = client.post('/products',
        json={'name': 'Test Product', 'price': 100.0, 'stock': 10})
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'Test Product'
    assert data['price'] == 100.0

def test_get_product(client):
    client.post('/products',
        json={'name': 'Test Product', 'price': 100.0, 'stock': 5})
    response = client.get('/products/1')
    assert response.status_code == 200

def test_delete_product(client):
    client.post('/products',
        json={'name': 'Test Product', 'price': 100.0, 'stock': 5})
    response = client.delete('/products/1')
    assert response.status_code == 200
