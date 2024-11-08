from django.urls import path
from . import views 
urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('register', views.RegisterUserView.as_view(), name="register_user"),
    path('register_book', views.RegisterBookView.as_view(), name="register_book"),
    path("list_books/", views.ListView.as_view(), name="list_books"),
    path("add_book_to_user/<int:id_user>/<int:id_book>/", views.AddBookToUserView.as_view(), name="add_book_to_user"),
    path("user_books/", views.UserBooksView.as_view(), name="user_books"),
]