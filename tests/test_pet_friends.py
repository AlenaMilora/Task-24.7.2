from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):

    status, result = pf.get_api_key(email, password)

    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter=''):

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0

def test_add_pet_without_photo_successfully(name='Karina', animal_type='Ragdoll', age='16'):

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_information_about_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name

def test_add_pet_without_photo_unsuccessfully(name='Bobik', animal_type='Ragdoll', age='16'):

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_information_about_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 500
    assert result['name'] == name

def test_add_photo_pet_with_valid_data(pet_id='3be476f3-2515-4c5a-8f83-2748f082944a',pet_photo='images/Karina.jpeg'):

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_photo_pet(auth_key, pet_id, pet_photo)

    assert status == 200
    assert result['pet_photo'] == pet_photo


