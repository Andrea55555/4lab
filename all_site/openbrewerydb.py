import pytest
import requests


@pytest.mark.parametrize('url_param,expected', [('https://api.openbrewerydb.org/breweries/madtree-brewing-cincinnati', 'MadTree Brewing'),
                                                ])
def test_list_checking_name(url_param, expected):
    """Проверяем наличие имени"""
    response = requests.get(url_param, expected)
    name = response.json()['name']
    assert name == expected


@pytest.mark.parametrize('url_param,expected', [('https://api.openbrewerydb.org/breweries?by_state=new_york', 20),
                                                ('https://api.openbrewerydb.org/breweries?by_state=new%20mexico', 20),
                                                ])
def test_assert_state(url_param, expected):
    """Проверка количества пивоварен по штатам, максимум отображается 20"""
    response = requests.get(url_param, expected)
    json_dict = response.json()
    assert len(json_dict) == expected


def test_assert_by_postal(url_param='https://api.openbrewerydb.org/breweries?by_postal=44107', expected=3):
    """Проверка количества пивоварен по почтовому индексу"""
    response = requests.get(url_param, expected)
    json_dict = response.json()
    assert len(json_dict) == expected


def test_assert_by_sity(url_param='https://api.openbrewerydb.org/breweries?by_city=san_diego', expected=20):
    """Проверка количества пивоварен по городу"""
    response = requests.get(url_param, expected)
    json_dict = response.json()
    assert len(json_dict) == expected


def test_assert_by_name(url_param='https://api.openbrewerydb.org/breweries?by_name=cooper', expected=16):
    """Проверка количества пивоварен по имени"""
    response = requests.get(url_param, expected)
    json_dict = response.json()
    assert len(json_dict) == expected