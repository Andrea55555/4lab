import pytest
import requests


def pytest_addoption(parser):
    """Параметры для тестов"""
    parser.addoption('--url',
                     action='store',
                     default='https://ya.ru',
                     help='Передайте url с помощью параметра --url')

    parser.addoption('--status_code',
                     action='store',
                     default='200',
                     help='Передайте status_code с помощью параметра --status_code')


@pytest.fixture
def url_param(request):
    """Фикстура для перадачи url"""
    return request.config.getoption('--url')


@pytest.fixture
def status_code(request):
    """Фикстура для перадачи status_code"""
    return request.config.getoption('--status_code')


def test_url_and_status_code(url_param, status_code):
    """Тест для проверки status_code"""
    response = requests.get(url_param)
    status_code = response.status_code
    assert status_code == 200
    print('status_code is OK ' + str(status_code))
