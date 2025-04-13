import pytest

from main import BooksCollector


class TestBooksCollector:


    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('input', ['', 'A'*41, 'A'*42, 'A'*100])
    def test_add_new_book_invalid_length(self, input, collector):
        collector.add_new_book(input)
        assert collector.get_books_genre() == {}

    def test_add_new_book_same_name(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_fantastic(self, collector):
        collector.add_new_book('Война миров')
        collector.set_book_genre('Война миров', 'Фантастика')
        assert collector.get_book_genre('Война миров') == 'Фантастика'

    def test_set_book_genre_invalid_book(self, collector):
        collector.set_book_genre('Мартин Иден', 'Фантастика')
        assert collector.get_book_genre('Мартин Иден') is None

    def test_set_book_genre_invalid_genre(self, collector):
        collector.add_new_book('Евгений Онегин')
        collector.set_book_genre('Евгений Онегин', 'Поэзия')
        assert collector.get_book_genre('Евгений Онегин') == ''

    def test_get_book_genre_detective(self, collector):
        collector.add_new_book('Убийство в «Восточном экспрессе»')
        collector.set_book_genre('Убийство в «Восточном экспрессе»', 'Детективы')
        assert collector.get_book_genre('Убийство в «Восточном экспрессе»') == 'Детективы'

    def test_get_books_with_specific_genre_cartoons(self, collector):
        collector.add_new_book('Том и Джерри')
        collector.add_new_book('Винни-Пух')
        collector.add_new_book('Война миров')
        collector.set_book_genre('Том и Джерри', 'Мультфильмы')
        collector.set_book_genre('Винни-Пух', 'Мультфильмы')
        collector.set_book_genre('Война миров', 'Фантастика')
        book_list = collector.get_books_with_specific_genre('Мультфильмы')
        assert len(book_list) == 2
        assert 'Том и Джерри' and 'Винни-Пух' in book_list


    def test_get_books_genre_valid_book(self, collector):
        collector.add_new_book('Бэтмен')
        collector.set_book_genre('Бэтмен', 'Фантастика')
        assert collector.get_books_genre() == {'Бэтмен': 'Фантастика'}

    def test_get_books_for_children_valid_age_rating(self, collector):
        collector.add_new_book('Маша и Медведь')
        collector.set_book_genre('Маша и Медведь', 'Мультфильмы')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        result = collector.get_books_for_children()
        assert len(result) == 1 and 'Маша и Медведь' in result
        assert 'Оно' not in result

    def test_add_book_in_favorites_added(self, collector):
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        assert 'Книга' in collector.get_list_of_favorites_books()


    def test_add_book_in_favorites_not_exist(self, collector):
        collector.add_book_in_favorites('Фантом')
        assert 'Фантом' not in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_same_book_not_added(self, collector):
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.add_book_in_favorites('Книга')
        result = collector.get_list_of_favorites_books()
        assert len(result) == 1


    def test_delete_book_from_favorites_deleted_exist_book(self, collector):
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.delete_book_from_favorites('Книга')
        assert 'Книга' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_valid(self, collector):
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.add_new_book('Книга1')
        collector.add_book_in_favorites('Книга1')
        assert collector.get_list_of_favorites_books() == ['Книга', 'Книга1']

