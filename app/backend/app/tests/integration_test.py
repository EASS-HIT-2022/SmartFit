from .utils.utils import create_random_item_with_owner, create_random_item_without_owner, random_lower_string, random_number_interval, user_authentication_headers
from fastapi.testclient import TestClient
from .routes.api.api_v1.endpoints.test_profile import test_create_user_profile,test_get_my_profile
import pytest 

@pytest.mark.integtest
def flow(client:TestClient,random_user):
	rand_user_headers = user_authentication_headers(client,email=random_user.email,password=random_user.password)
	test_create_user_profile(client,rand_user_headers)
	test_get_my_profile(client,rand_user_headers)

