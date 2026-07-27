from main import BooksCollector
import pytest # класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_same_book_not_added_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Дюна')
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('name', ['', 'А' * 41])
    def test_add_new_book_invalid_name_not_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert collector.get_books_genre() == {}

    def test_set_book_genre_is_set(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_book_genre('Дюна') == 'Фантастика'

    def test_get_books_with_specific_genre_returns_book_with_requested_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('ОНО')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('ОНО', 'Ужасы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Дюна']