import pytest
from new_user_data import generate_user_data
from api_shop import ApiShop
import helpers


@pytest.fixture
def create_user():
    user_data = generate_user_data()
    user_creation = ApiShop.create_user(user_data)
    token = user_creation.json()['accessToken']
    yield [user_data, user_data["email"], user_data["password"], token]
    ApiShop.delete_user(token)


@pytest.fixture
def collect_ingredients_hash():
    response = ApiShop.get_ingredients_hash()
    ingredients_list = {"ingredients": [response['data'][helpers.random_int]['_id'],
                                        response['data'][helpers.random_int]['_id'],
                                        response['data'][helpers.random_int]['_id']]}
    yield ingredients_list