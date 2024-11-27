import allure
from data import ErrorMessageText
from api_shop import ApiShop


class TestGetOrders:

    @allure.title('Successful orders list get for authorized user test')
    def test_get_orders_auth_user(self, create_user, collect_ingredients_hash):
        ApiShop.create_order_auth(collect_ingredients_hash, create_user[3])
        response = ApiShop.get_orders_auth(create_user[3])
        assert response.status_code == 200 and "orders" in response.text

    @allure.title('Orders list get failed for non auth user test')
    def test_get_orders_non_auth_user(self):
        response = ApiShop.get_orders_no_auth()
        assert response.status_code == 401 and response.json()['message'] == ErrorMessageText.GET_ORDERS_ERROR