from books_app import app

from books_app.controllers import Authors
from books_app.controllers import Books

if __name__ == '__main__':
    app.run(debug = True)