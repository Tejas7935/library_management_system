from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)

class Book(models.Model):
    name = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)
    categories = models.ManyToManyField(Category)
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.name) + " [" + str(self.isbn) + ']'

class Language(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return '{0}, {1}'.format(self.last_name, self.first_name)
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    branch = models.CharField(max_length=10)
    roll_no = models.CharField(max_length=3, blank=True)
    phone = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return str(self.user) + " [" + str(self.branch) + ']' + " [" + str(
            self.roll_no) + ']'
def expiry():
    return datetime.today() + timedelta(days=15)

class IssuedBook(models.Model):
    student = models.ForeignKey('Student',on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey('Book',on_delete=models.SET_NULL, null=True)
    issued_date = models.DateField(auto_now=True)
    return_date = models.DateField(default=expiry)