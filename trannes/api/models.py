from django.db import models

# Create your models here.
class Users(models.Model):
    user_id = models.CharField(primary_key=True, max_length=32)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users'

class UserDetails(models.Model):
    user_id = models.CharField(primary_key=True, max_length=32)
    user_name = models.CharField(max_length=32)
    mail_address = models.CharField(max_length=255)
    gender = models.CharField(max_length=8)
    birthday = models.DateField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_details'

class Books(models.Model):
    isbn_id = models.CharField(primary_key=True, max_length=13)
    book_title = models.CharField(max_length=255)
    book_author = models.CharField(max_length=255)
    book_detail = models.CharField(max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'books'

class BookGenres(models.Model):
    isbn_id = models.CharField(max_length=13)
    book_genre = models.CharField(max_length=255)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'book_genres'

class UserBooks(models.Model):
    user_id = models.CharField(max_length=32)
    isbn_id = models.CharField(max_length=13)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_books'

class UserLists(models.Model):
    list_id = models.AutoField(primary_key=True)
    list_name = models.CharField(max_length=32)
    user_id = models.CharField(max_length=32)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_lists'

class UsersListBooks(models.Model):
    list_id = models.IntegerField()
    isbn_id = models.CharField(max_length=13)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users_list_books'

class SearchHistory(models.Model):
    user_id = models.CharField(max_length=32)
    search_word = models.CharField(max_length=255)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'search_history'