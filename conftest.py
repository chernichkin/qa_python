import pytest
from main import BooksCollector

@pytest.fixture(scope='function') #запускаем перед каждым тестом
def collector():
    collector = BooksCollector()
    return collector
