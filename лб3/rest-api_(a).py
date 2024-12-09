from flask import Flask, jsonify

app = Flask(__name__)
catalog = [
    {"id": 1, "name": "Espresso", "price": "100"},
    {"id": 2, "name": "Cappuccino", "price": "80.00"},
    {"id": 3, "name": "Americano", "price": "50.00"}
]
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(catalog)
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((i for i in catalog if i["id"] == item_id))
    return jsonify(item)
if __name__ == '__main__':
    app.run(debug=True)