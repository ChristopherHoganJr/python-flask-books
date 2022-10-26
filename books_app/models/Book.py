from books_app.config.mysqlconnection import connectToMySQL
from books_app import app

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_new_book(cls, data):
        query = 'INSERT INTO books (title, num_of_pages, created_at, updated_at) VALUES (%(title)s, %(num_of_pages)s, NOW(), NOW());'
        return connectToMySQL('books_python').query_db(query, data)

    @classmethod
    def get_all_books(cls):
        query = 'SELECT * FROM books'
        return connectToMySQL('books_python').query_db(query)

    @classmethod
    def get_single_book(cls, data):
        query = 'SELECT title FROM books WHERE id = %(id)s;'
        return connectToMySQL('books_python').query_db(query, data)

    @classmethod
    def get_book_favorites(cls, data):
        query = 'SELECT * FROM books JOIN favorites ON favorites.books_id = books.id LEFT JOIN authors ON authors.id = favorites.authors_id WHERE books.id = %(id)s;'
        results = connectToMySQL('books_python').query_db(query, data)
        fav_authors = []
        for fav_author in results:
            print(fav_author)
            author = {
                'name':fav_author['name'],
                'id':fav_author['books_id']
            }
            fav_authors.append(author)
        return fav_authors
