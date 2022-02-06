import pytest
import requests


def test_list_all_image(url_param='https://dog.ceo/api/breed/hound/images', expected=1000):
    """Проверяем сколько всего кратинок"""
    response = requests.get(url_param)
    message = response.json()['message']
    assert len(message) == expected


def test_list_all_bread_dogs(url_param='https://dog.ceo/api/breeds/list/all', expected=95):
    """Проверяем сколько всего пород собак"""
    response = requests.get(url_param)
    message = response.json()['message']
    assert len(message) == expected


def test_list_all_image_afgan(url_param='https://dog.ceo/api/breed/hound/afghan/images', expected=239):
    """Проверяем сколько всего кратинок афганской собаки"""
    response = requests.get(url_param)
    message = response.json()['message']
    assert len(message) == expected


@pytest.mark.parametrize('url_param,expected', [('https://dog.ceo/api/breeds/image/random', 'success'),
                                                ])
def test_list_checking_status(url_param, expected):
    """Проверяем статус"""
    response = requests.get(url_param, expected)
    status = response.json()['status']
    assert status == expected


@pytest.mark.parametrize('url_param,expected', [('https://dog.ceo/api/breeds/image/random', 'null'),
                                                ])
def test_list_all_bread_dogs_with_params(url_param, expected):
    """Проверяем, что рандомная картинка не пустая"""
    response = requests.get(url_param, expected)
    json_dict = response.json()
    assert len(json_dict) != expected


""""""
