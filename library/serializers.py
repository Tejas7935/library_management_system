from rest_framework import serializers

from library.models import Student, Book, Author


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['branch',  'roll_no', 'phone']


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['isbn', 'name', 'author', 'language', 'categories']

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']