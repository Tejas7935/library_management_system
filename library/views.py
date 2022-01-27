from rest_framework import viewsets
from rest_framework import permissions

from library.models import Student, Book, Author
from library.serializers import UserSerializer, BookSerializer, AuthorSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = UserSerializer





class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]



class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]
