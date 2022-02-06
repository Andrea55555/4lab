import pytest
import requests


@pytest.mark.parametrize('url_param,expected', [('https://jsonplaceholder.typicode.com/todos/1', False),
                                                ])
def test_list_checking_status(url_param, expected):
    """Проверяем,что completed = false"""
    response = requests.get(url_param, expected)
    completed = response.json()['completed']
    assert completed == expected


@pytest.mark.parametrize('url_param,expected', [('https://jsonplaceholder.typicode.com/todos/1', "delectus aut autem"),
                                                ])
def test_list_checking_status(url_param, expected):
    """Проверяем?что d title нужный текст"""
    response = requests.get(url_param, expected)
    title = response.json()['title']
    assert title == expected


def test_assert_users(url_param='https://jsonplaceholder.typicode.com/users', expected=10):
    """Проверяем количество пользователей"""
    response = requests.get(url_param)
    users = response.json()
    fact_list = []
    for element in users:
        fact_list.append(element['id'])
    assert len(fact_list) == expected


def test_assert_todos(url_param='https://jsonplaceholder.typicode.com/posts/1/todos', expected=200):
    """Проверясм количество todos"""
    response = requests.get(url_param)
    json_dict = response.json()
    fact_list = []
    for element in json_dict:
        fact_list.append(element['id'])
    assert len(fact_list) == expected


def test_assert_albums(url_param='https://jsonplaceholder.typicode.com/posts/1/albums', expected=100):
    """Проверясм количество альбомов"""
    response = requests.get(url_param)
    json_dict = response.json()
    fact_list = []
    for element in json_dict:
        fact_list.append(element['id'])
    assert len(fact_list) == expected