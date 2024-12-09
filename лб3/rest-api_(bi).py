from flask import Flask, jsonify, request, Response
from functools import wraps

app = Flask(__name__)
users = {"admin": "admin123", "user": "user123"}
catalog = [
    {"id": 1, "name": "Espresso", "price": "100"},
    {"id": 2, "name": "Cappuccino", "price": "80.00"},
    {"id": 3, "name": "Americano", "price": "50.00"}
]
def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username in users and users[auth.username] == auth.password:
            return func(*args, **kwargs)
        return Response("Потрібна автентифікація!", status=401, headers={"WWW-Authenticate": "Basic"})
    return wrapper

@app.route('/items', methods=['GET'])
@authenticate
def get_items():
    return jsonify(catalog)
@app.route('/items/<int:item_id>', methods=['GET'])
@authenticate
def get_item(item_id):
    item = next((i for i in catalog if i["id"] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)

if __name__ == '__main__':
    app.run(debug=True)
