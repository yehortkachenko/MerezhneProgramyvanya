import requests

BASE_URL = "http://127.0.0.1:5000/items"

def get_catalog():
    """Отримати весь каталог товарів."""
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        print("Каталог товарів:")
        for item in response.json():
            print(item)
    else:
        print(f"Помилка отримання каталогу: {response.status_code}")

def add_item(item):
    """Додати новий товар."""
    response = requests.post(BASE_URL, json=item)
    if response.status_code == 201:
        print("Товар успішно додано:")
        print(response.json())
    else:
        print(f"Помилка додавання товару: {response.status_code}, {response.json()}")

def update_item(item_id, updated_data):
    """Оновити товар за ID."""
    response = requests.put(f"{BASE_URL}/{item_id}", json=updated_data)
    if response.status_code == 200:
        print("Товар успішно оновлено:")
        print(response.json())
    else:
        print(f"Помилка оновлення товару: {response.status_code}, {response.json()}")

def delete_item(item_id):
    """Видалити товар за ID."""
    response = requests.delete(f"{BASE_URL}/{item_id}")
    if response.status_code == 200:
        print("Товар успішно видалено:")
        print(response.json())
    else:
        print(f"Помилка видалення товару: {response.status_code}, {response.json()}")

# Приклади використання:
if __name__ == "__main__":
    get_catalog()
    new_item = {"id": 4, "name": "Latte", "price": "70.00"}
    add_item(new_item)
    updated_item = {"name": "Latte Updated", "price": "75.00"}
    update_item(4, updated_item)
    delete_item(4)
    get_catalog()
