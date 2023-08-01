import config
import requests
import test_orders

# Выполняем запрос на получение заказа по треку заказа
def new_request(track_id):
    return requests.get(config.URL_SERVICE + config.GET_ORDER + str(test_orders.track_id))

response = new_request(test_orders.track_id)
assert response.status_code == 200
print(response.status_code)

