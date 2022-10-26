from books_app import app
from flask import render_template, request, redirect
from books_app.models.Author import Author
from books_app.models.Book import Book

@app.route('/authors')
def authors_main():
    all_authors = Author.get_all_authors()
    return render_template('allAuthors.html', all_authors=all_authors)

@app.route('/authors/new/submit', methods=['post'])
def add_new_author():
    data = {
        'name':request.form['name'],
    }
    Author.create_new_author(data)
    return redirect('/authors')

@app.route('/authors/<int:id>')
def author_favorites(id):
    author_name = Author.get_single_author({'id':id})
    favorite_books = Author.get_author_favorites({'id':id})
    all_books = Book.get_all_books()
    return render_template('authorShow.html', favorite_books=favorite_books, author_name=author_name[0], all_books=all_books)

@app.route('/authors/favorite/submit/<int:id>', methods=['post'])
def add_favorite_book(id):
    data = {'books_id':request.form['book_id'],
            'authors_id':str(id)
    }
    Author.author_add_favorite(data)
    return redirect('/authors/'+str(id))