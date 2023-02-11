import pytest

class User:
    def __init__(self) -> None:
        self.name = 'Alina'
        self.second_name = 'Dreksler'

@pytest.fixture
def user():
    yield User()

def test_remove_name(user) :
    user.name = ''
    assert user.name =='' 

def test_name(user):
    assert user.name == 'Alina' 

def test_second_name(user):
    assert user.secind_name == 'Dreksler'      