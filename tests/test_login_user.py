import pytest
import allure
from api_shop import ApiShop
from data import ErrorMessageText


class TestUserLogin:

    @allure.title('Successful user login test')
    def test_user_login_success(self, create_user):
        login_data = {'email': create_user[1], 'password': create_user[2]}
        response = ApiShop.login_user(login_data)
        assert response.status_code == 200 and (response.json()['success'] == True)

    @allure.title('Wrong user password error test')
    def test_user_login_with_wrong_password(self, create_user):
        login_data = {'email': create_user[1], 'password': 'test_password'}
        response = ApiShop.login_user(login_data)
        assert response.status_code == 401 and (response.json()['message'] == ErrorMessageText.INCORRECT_DATA)