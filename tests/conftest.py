import pytest
import requests
from configuration import SERVICE_URL1
from random import randrange
# название файла только conftest!
@pytest.fixture #фикстура будет происходить перед каждым тестом где она есть
def get_users():
    response = requests.get(url=SERVICE_URL1)
    return response

def _calculate(a, b):
    return a+b
@pytest.fixture
def calculate():
    return _calculate

@pytest.fixture  # setup и teardown - создание и удаление в начале и конце теста соответсвтенно (например новый юзер в БД)
def make_number():
    print("I'm getting number")
    number = randrange (1, 1000, 5)
    yield number       # передача данных и дальнейшего управления основному тесту
    print(f"Number at home {number}") # выполнится после основного теста


# @pytest.fixture(scope='function') # function - стоит по умолчанию и выполняет фикстуру каждый раз, session - выполняется 1 раз и кэшируется
# def say_hello():
#     print('hello')
#     return 14

# @pytest.fixture(autouse=True) #автоматическое выполнение, False стоит по умолчанию. фикстура будет выполняться для каждого теста и без ее указания там
# def say_hello():
#     print('hello')
#     return 14