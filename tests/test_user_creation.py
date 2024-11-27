import pytest
import allure
from new_user_data import generate_user_data, WrongUserData
from api_shop import ApiShop
from data import ErrorMessageText


class TestCreateUser:

    @allure.title('Successful creation of new user')
    def test_create_user_success(self):
        body = generate_user_data()
        creation_user = ApiShop.create_user(body)
        token = creation_user.json()['accessToken']
        assert creation_user.status_code == 200 and ('accessToken' in creation_user.json())
        ApiShop.delete_user(token)

    @allure.title('Creation User Clone Error')
    def test_create_user_clone_error(self, create_user):
        response = ApiShop.create_user(create_user[0])
        assert response.status_code == 403 and (response.json()['message'] == ErrorMessageText.USER_ALREADY_EXIST)

    @allure.title('Error of User registration with deficit data')
    @pytest.mark.parametrize('data', WrongUserData.wrong_data)
    def test_create_user_deficit_data_error(self, data):
        response = ApiShop.create_user(data)
        assert response.status_code == 403 and (response.json()['message'] == ErrorMessageText.DEFICIT_DATA)