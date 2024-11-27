import allure
import pytest
from api_shop import ApiShop
from data import ErrorMessageText
from new_user_data import generate_user_data, SingleDataFiled


class TestUpdateUserData:

    @allure.title('Successful user data update')
    @pytest.mark.parametrize('data_field, new_data', (['email', SingleDataFiled.email], [
        'name', SingleDataFiled.name], ["password", SingleDataFiled.password]))
    def test_update_user_data_success(self, create_user, data_field, new_data):
        create_user[0][data_field] = new_data
        response = ApiShop.update_user_data_with_token(create_user[3], create_user[0])
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title('Non auth user data update failed test')
    def test_update_user_data_non_auth_error(self, create_user):
        updated_user_data = generate_user_data()
        response = ApiShop.update_user_data_no_token(updated_user_data)
        assert response.status_code == 401 and response.json()['message'] == ErrorMessageText.USER_DATA_UPDATE_ERROR