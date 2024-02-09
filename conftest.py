import pytest
from endpoints.base_method import Api
from endpoints.get_getting_resource import GettingResource
from endpoints.get_listing_all_resources import ListingAllResources
from endpoints.post_сreating_resource import CreatingResource
from endpoints.put_updating_resource import UpdatingResource
from endpoints.patch_patching_resource import PatchingResource
from endpoints.delete_deleting_resource import DeletingResource


@pytest.fixture(scope="session")
def api():
    base_url = "https://jsonplaceholder.typicode.com/"
    return Api(base_url=base_url)


@pytest.fixture
def getting_resource(api):
    return GettingResource(api)


@pytest.fixture
def listing_resources(api):
    return ListingAllResources(api)


@pytest.fixture
def creating_resource(api):
    return CreatingResource(api)


@pytest.fixture
def updating_resource(api):
    return UpdatingResource(api)


@pytest.fixture
def patching_resource(api):
    return PatchingResource(api)


@pytest.fixture
def daleting_resource(api):
    return DeletingResource(api)
