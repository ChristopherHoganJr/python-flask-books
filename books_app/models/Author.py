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
    def get_all_authors(cls):
        query = 'SELECT * FROM authors;'
        return connectToMySQL('books_python').query_db(query)