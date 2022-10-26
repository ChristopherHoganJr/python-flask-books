from sqlite3 import connect
from books_app.config.mysqlconnection import connectToMySQL
from books_app import app

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_new_author(cls, data):
        query = 'INSERT INTO authors (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());'
        return connectToMySQL('books_python').query_db(query, data)

    @classmethod
    def get_single_author(cls, data):
        query = 'SELECT name FROM authors WHERE id = %(id)s;'
        return connectToMySQL('books_python').query_db(query, data)

    @classmethod
    def get_all_authors(cls):
        query = 'SELECT * FROM authors;'
        return connectToMySQL('books_python').query_db(query)

    @classmethod
    def get_author_favorites(cls, data):
        query = 'SELECT * FROM authors JOIN favorites ON favorites.authors_id = authors.id LEFT JOIN books ON books.id = favorites.books_id WHERE authors.id = %(id)s;'
        results = connectToMySQL('books_python').query_db(query, data)
        fav_books = []
        for fav_book in results:
            book = {
                'name':fav_book['name'],
                'title':fav_book['title'],
                'num_of_pages':fav_book['num_of_pages'],
            }
            fav_books.append(book)
        return fav_books

    @classmethod
    def author_add_favorite(cls, data):
        query = 'INSERT INTO favorites (authors_id, books_id) VALUES (%(authors_id)s, %(books_id)s);'
        return connectToMySQL('books_python').query_db(query, data)