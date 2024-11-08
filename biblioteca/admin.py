from django.contrib import admin
from biblioteca.models import Users, Books, UserBooks

admin.site.register(Users)
admin.site.register(Books)
admin.site.register(UserBooks)
# Register your models here.
