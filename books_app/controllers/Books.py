from books_app import app
from flask import render_template, request, redirect
from books_app.models.Book import Book

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