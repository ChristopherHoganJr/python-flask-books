from books_app import app
from flask import render_template, request, redirect
from books_app.models.Author import Author

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