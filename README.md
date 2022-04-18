# The Book API
This repository contains Book API written by Django/Django Rest Framework. 
It is a RESTful API that provides CRUD operations for books, authors and categories.

# Using Tools
 - Django
 - Django Rest Framework
 - django-filters

# Database
App uses file based Sqlite database. You can find database file in the project root.

## Clone the project and Install the dependencies
```
$ git clone https://github.com/eibrahimarisoy/book-api.git
$ cd book-api
$ pip install -r requirements.txt
```

 ## Run the project
```
$ cd book-api
$ python manage.py runserver
```

## Routes
Default **BookStore API** routes are listed below. 
  
| METHOD   | ROUTE              | DETAILS                      |
|----------|--------------------|------------------------------|
| POST     | /api/books         | Create a new book.           |
| GET      | /api/books         | List all books.              |
| PUT      | /api/books         | Update a book.               |
| PATCH    | /api/books         | Partially update a book.     |
| DELETE   | /api/books         | Delete a book.               |
| POST     | /api/authors       | Create a new author.         |
| GET      | /api/authors       | List all authors             |
| PUT      | /api/authors       | Update a author.             |
| PATCH    | /api/authors       | Partially update a author.   |
| DELETE   | /api/authors       | Delete a author.             |
| POST     | /api/categories    | Create a new category.       |
| GET      | /api/categories    | List all categorys.          |
| PUT      | /api/categories    | Update a category.           |
| PATCH    | /api/categories    | Partially update a category. |
| DELETE   | /api/categories    | Delete a category.           |

## Contact

If you want to contact me you can reach me at <eibrahimarisoy@gmail.com>.