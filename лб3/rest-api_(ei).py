from flask import Flask, jsonify, request

app = Flask(__name__)
catalog = [
    {"id": 1, "name": "Espresso", "price": "100"},
    {"id": 2, "name": "Cappuccino", "price": "80.00"},
    {"id": 3, "name": "Americano", "price": "50.00"}
]
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(catalog)
if __name__ == '__main__':
    app.run(debug=True)
# GET http://127.0.0.1:5000/items