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