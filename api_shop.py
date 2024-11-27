import requests
from data import Url


class ApiShop:

    @staticmethod
    def create_user(body):
        return requests.post(f'{Url.MAIN_URL}{Url.CREATE_USER}', json=body)

    @staticmethod
    def delete_user(token):
        return requests.delete(f'{Url.MAIN_URL}{Url.DELETE_USER}', headers={'Authorization': token})

    @staticmethod
    def login_user(body):
        return requests.post(f'{Url.MAIN_URL}{Url.LOGIN}', json=body)

    @staticmethod
    def update_user_data_with_token(token, body):
        return requests.patch(f'{Url.MAIN_URL}{Url.UPDATE_USER_DATA}', json=body, headers={
            'Authorization': token})

    @staticmethod
    def update_user_data_no_token(body):
        return requests.patch(f'{Url.MAIN_URL}{Url.UPDATE_USER_DATA}', json=body)

    @staticmethod
    def get_ingredients_hash():
        return requests.get(f'{Url.MAIN_URL}{Url.GET_INGREDIENTS}').json()

    @staticmethod
    def create_order_auth(body, token):
        return requests.post(f'{Url.MAIN_URL}{Url.CREATE_ORDER}', json=body, headers={
            'Authorization': token})

    @staticmethod
    def create_order_non_auth(body):
        return requests.post(f'{Url.MAIN_URL}{Url.CREATE_ORDER}', json=body)

    @staticmethod
    def get_orders_auth(token):
        return requests.get(f'{Url.MAIN_URL}{Url.GET_ORDERS}', headers={
            'Authorization': token})

    @staticmethod
    def get_orders_no_auth():
        return requests.get(f'{Url.MAIN_URL}{Url.GET_ORDERS}')