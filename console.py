import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("Suzanne", "Collins")
author_repository.save(author1)

author2 = Author("J.R.R.", "Tolkien")
author_repository.save(author2)

book1 = Book("The Hunger Games", "Young Adult", "Scholastic", author1)
book_repository.save(book1)

book2 = Book("The Lord of the Rings", "Fantasy", "Harper Collins", author2)
book_repository.save(book2)

book3 = Book("The Hobbit", "Fantasy", "Harper Collins", author2)
book_repository.save(book3)

book4 = Book("Silmarillion", "Fantasy", "Christopher Tolkien", author2)
book_repository.save(book4)

pdb.set_trace()