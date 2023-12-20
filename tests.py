import pytest
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    books_for_children = [['Пинокио', 'Мультфильмы'], ['Марли и я', 'Комедии'], ['Интерселлар', 'Фантастика']]
    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
        # создаем экземпляр (объект) класса BooksCollector - тут убрал
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2  #тут поменял метод из прекода на get_books_genre, get_books_rating не существует

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_get_books_genre_get_one_gener_true(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Комедии')
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_one_gener_checked_true(self, collector):
        genre = 'Комедии'
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Комедии')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == genre

    def test_get_books_with_specific_genre_one_gener_true(self, collector):
        book = 'Что делать, если ваш кот хочет вас убить'
        collector.add_new_book(book)
        collector.set_book_genre(book, 'Фантастика')
        assert book in collector.get_books_with_specific_genre('Фантастика')

    def test_get_books_with_specific_genre_two_books_in_list_true(self, collector):

        collector.add_new_book('Что делать если ваш рабочий день 3 часа')
        collector.add_new_book('Жена без истерик')
        collector.set_book_genre('Что делать если ваш рабочий день 3 часа', 'Фантастика')
        collector.set_book_genre('Жена без истерик', 'Фантастика')
        assert len(collector.get_books_with_specific_genre('Фантастика')) == 2

    @pytest.mark.parametrize('bookname,bookgenre', books_for_children)
    def test_get_books_for_children_check_all_genre_true(self,collector, bookname, bookgenre):
        collector.add_new_book(bookname)
        collector.set_book_genre(bookname, bookgenre)
        assert len(collector.get_books_for_children()) == 1

    def test_get_books_for_children_one_books_in_list_true(self, collector):
        collector.add_new_book('Вниз!')
        collector.set_book_genre('Вниз!', 'Мультфильмы')
        assert len(collector.get_books_for_children()) == 1 and collector.get_book_genre('Вниз!') == 'Мультфильмы'

    def test_get_books_for_children_one_adult_book_in_list_false(self, collector):
        collector.add_new_book('Валли')
        collector.set_book_genre('Валли', 'Ужасы')
        assert not len(collector.get_books_for_children()) == 1

    def test_get_book_genre_book_has_no_genre_true(self, collector):
        collector.add_new_book('Нуу.. бывает не понятно..')
        assert collector.get_book_genre('Нуу.. бывает не понятно..') == ''

    @pytest.mark.parametrize('bookname,bookgenre', books_for_children)
    def test_add_book_in_favorites_one_book_true(self, collector, bookname, bookgenre):
        collector.add_new_book(bookname)
        collector.set_book_genre(bookname, bookgenre)
        collector.add_book_in_favorites(bookname)
        assert len(collector.get_list_of_favorites_books()) == 1

    @pytest.mark.parametrize('bookname,bookgenre', books_for_children)
    def test_add_book_in_favorites_one_book_false(self, collector, bookname, bookgenre):
        collector.add_new_book(bookname)
        collector.set_book_genre(bookname, bookgenre)
        assert not len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_one_book_without_genre(self, collector):
        collector.add_new_book('Нуу.. бывает не понятно..')
        collector.add_book_in_favorites('Нуу.. бывает не понятно..')
        collector.delete_book_from_favorites('Нуу.. бывает не понятно..')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_add_new_book_with_more_then_40_simbols(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби fdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd')
        assert len(collector.get_books_genre()) == 0
