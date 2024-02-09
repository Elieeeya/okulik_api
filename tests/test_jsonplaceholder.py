import time


def test_get_user(getting_resource):
    getting_resource.get_user()


def test_get_all_users(listing_resources):
    listing_resources.get_all_users()


def test_post_new_user(creating_resource):
    creating_resource.new_users()


def test_put_update_user(creating_resource, updating_resource):
    creating_resource.new_users()
    updating_resource.update_users()


def test_patch_update_user(creating_resource, updating_resource, patching_resource):
    creating_resource.new_users()
    updating_resource.update_users()
    patching_resource.part_update_users()


def test_delete_user(creating_resource, updating_resource, patching_resource, daleting_resource):
    creating_resource.new_users()
    updating_resource.update_users()
    patching_resource.part_update_users()
    daleting_resource.delete_users()
