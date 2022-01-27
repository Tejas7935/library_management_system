from django.contrib import admin

from .models import Book
from .models import Student
from .models import Category
from .models import Language
from .models import Author
from .models import IssuedBook

admin.site.register([Book, Student, Category, Language, Author, IssuedBook ])


