from django.db import models
from django.utils.translation import gettext_lazy as _
from django import forms
from django.utils import timezone


class Users(models.Model):
    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
    id_user = models.AutoField(primary_key=True, verbose_name=_("ID"))
    user_name = models.CharField(max_length=40, verbose_name=_("Username"))
    user_email = models.EmailField(max_length=255, verbose_name=_("Email"))
    user_password = models.CharField(max_length=255, verbose_name=_("Password"))
    user_age = models.IntegerField(verbose_name=_("Age"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Creation date"))
     
    def __str__(self):
        return self.user_name
    
class Books(models.Model):
    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")
    id_book = models.AutoField(primary_key=True, verbose_name=_("ID"))
    book_title = models.CharField(max_length=100, verbose_name=_("Title"))
    editorial = models.CharField(max_length=100, verbose_name=_("Editorial"))
    published_at = models.DateTimeField(null=True, blank=True, verbose_name=_("Published at"))
    
    def __str__ (self):
        return self.book_title
    
class UserBooks(models.Model):
    class Meta:
        verbose_name = _("User book")   
        verbose_name_plural = _("User books")
        unique_together = ('id_user', 'id_books')
    id_user_book = models.AutoField(primary_key=True , verbose_name=_("ID"))
    id_user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name=_("ID"))
    id_books = models.ForeignKey(Books, on_delete=models.CASCADE, verbose_name=_("ID"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Creation date"))