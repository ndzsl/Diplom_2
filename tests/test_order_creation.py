import allure
from api_shop import ApiShop
from data import ErrorMessageText
from order_data import OrderData


class TestCreateOrder:

    @allure.title('Successful order creation with authorization')
    def test_create_order_with_auth_success(self, create_user, collect_ingredients_hash):
        response = ApiShop.create_order_auth(collect_ingredients_hash, create_user[3])
        assert response.status_code == 200 and response.json()["success"] == True

    @allure.title('Successful order creation with no authorization')
    def test_create_order_with_no_auth_success(self, collect_ingredients_hash):
        response = ApiShop.create_order_non_auth(collect_ingredients_hash)
        assert response.status_code == 200 and response.json()["success"] == True

    @allure.title('Order creation without ingredients and auth error test')
    def test_create_order_no_ingredients_no_auth(self):
        response = ApiShop.create_order_non_auth(OrderData.empty_ingredients)
        assert response.status_code == 400 and response.json()['message'] == ErrorMessageText.NOT_ENOUGH_INGREDIENTS

    @allure.title('Order creation without ingredients but with auth error test')
    def test_create_order_no_ingredients_with_auth(self, create_user):
        response = ApiShop.create_order_auth(OrderData.empty_ingredients, create_user[3])
        assert response.status_code == 400 and response.json()['message'] == ErrorMessageText.NOT_ENOUGH_INGREDIENTS

    @allure.title('Order creation with wrong ingredients hash error test')
    def test_create_order_with_wrong_ingredients(self):
        response = ApiShop.create_order_non_auth(OrderData.invalid_ingredients)
        assert response.status_code == 500