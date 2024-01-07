# qa_python
Что сделано:
1. Использовал параметризацию
2. Добавил одну простейшую фикстуру
3. Исправил ошибку в прекоде для test_add_new_book_add_two_books
Добавлены следующие тесты:
1. test_add_new_book_add_two_books
Тест на проверку добавления двух книг из прекода
2. test_get_books_genre_get_one_gener_true
Тест на проверку добавление одного жанра
3. test_set_book_genre_one_gener_checked_true
Тест на проверку добавления конкретного жанра
4. test_get_books_with_specific_genre_one_gener_true
Тест на проверку отображения конкретной книги в специальном жанре
5. test_get_books_with_specific_genre_two_books_in_list_true
Тест на проверку что в специальном жанре отображается 2 книги после их добавления
6.test_get_books_for_children_check_all_genre_true
Тест что у детей отображаются все соответсвующие жанры(использовал параметризацию)
7.test_get_books_for_children_one_books_in_list_true
Тест на отображение одной книги в списке для детей
8. test_get_books_for_children_one_adult_book_in_list_false
Тест на отображение пустого списка у детей при добавлении одной книги с жанром для взрослых
9. test_add_book_in_favorites_one_book_true
Тест на добавление одной книги в избранное
10. test_add_book_in_favorites_one_book_false
Тест на отсутсвие книг в избранном без её добавления в него
11. test_delete_book_from_favorites_one_book_without_genre
Тест на удаление книг из списка избранного
12. test_add_new_book_with_more_then_40_simbols
Тест что не добавляются книги с более 40 символов в названии
