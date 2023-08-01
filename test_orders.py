import config
import docs
import requests

# Создание заявки
def new_order():
    return requests.post(config.URL_SERVICE + config.NEW_ORDER, json=docs.body_order)
    result = response.json()
    track_id = result.get("track")
    return track_id

# Вызываем функцию для получения номера заказа
track_id = new_order()
print(track_id.json())



