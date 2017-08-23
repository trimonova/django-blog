from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
class Book():
    def __init__(self, author, title, description, rating, imageUrl):
        self.author = author
        self.title = title
        self.description = description
        self.rating = rating
        self.imageUrl = imageUrl

    def __repr__(self, *args, **kwargs):
        return self.author + '\n' + self.title + '\n'


class BooksModel():
    def __init__(self):
        self.books = []