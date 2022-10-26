from books_app import app
from flask import render_template, request, redirect
from books_app.models.Book import Book
from books_app.models.Author import Author

@app.route('/books')
def books_main():
    all_books = Book.get_all_books()
    return render_template('allBooks.html',all_books=all_books)

@app.route('/books/new/submit', methods=['post'])
def add_new_book():
    data = {
        'title':request.form['title'],
        'num_of_pages':request.form['num_of_pages']
    }
    Book.create_new_book(data)
    return redirect('/books')

@app.route('/books/<int:id>')
def bookShow(id):
    book_title = Book.get_single_book({'id':id})
    fav_authors = Book.get_book_favorites({'id':id})
    all_authors = Author.get_all_authors()

    return render_template('bookShow.html', book_title=book_title[0], all_authors=all_authors, fav_authors=fav_authors)

@app.route('/books/favorite/submit/<int:id>', methods=['post'])
def add_favorite_author(id):
    data = {
        'authors_id':request.form['authors_id'],
        'books_id':str(id)
    }
    Author.author_add_favorite(data)
    return redirect('/books/'+str(id))