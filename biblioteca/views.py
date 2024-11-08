from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Users, Books, UserBooks
from .api.serializers import UsersSerializers, BooksSerializers, UsersBooksSerializers

class HomeView(APIView):
    def get(self, request):
        return Response("Home")

# View de registro de usuário
class RegisterUserView(APIView):
    def get(self, request):
        # Renderiza o formulário de registro de usuário
        return render(request, "biblioteca/register.html")

    def post(self, request):
        # Cria um novo usuário com base nos dados do request
        serializer = UsersSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Retorna os dados do usuário em formato JSON após a criação
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Se os dados forem inválidos, retorna os erros
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View de registro de livro
class RegisterBookView(APIView):
    def get(self, request):
        # Renderiza o formulário de registro de livro
        return render(request, "biblioteca/register_book.html")

    def post(self, request):
        # Cria um novo livro com base nos dados do request
        serializer = BooksSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Retorna os dados do livro em formato JSON após a criação
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Se os dados forem inválidos, retorna os erros
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View para associar livros ao usuário
class RegisterUserBooksView(APIView):
    def get(self, request):
        # Renderiza o formulário de associação de livros a um usuário
        return render(request, "biblioteca/register_user_book.html")

    def post(self, request):
        # Cria uma associação de livro ao usuário com base nos dados do request
        serializer = UsersBooksSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Retorna os dados da associação em formato JSON após a criação
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Se os dados forem inválidos, retorna os erros
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View para listar todos os livros
class ListView(APIView):
    def get(self, request):
        # Obtém todos os livros no banco de dados
        books = Books.objects.all()
        # Retorna todos os livros como JSON
        serializer = BooksSerializers(books, many=True)
        return Response(serializer.data)

# View para adicionar um livro ao usuário
class AddBookToUserView(APIView):
    def post(self, request, id_user, id_book):
        try:
            user = Users.objects.get(id_user=id_user)
            book = Books.objects.get(id_book=id_book)
            # Cria a associação entre o livro e o usuário
            user_book = UserBooks.objects.create(id_user=user, id_books=book)
            user_book.save()
            return Response(f"Book '{book.book_title}' added to user '{user.user_name}'", status=status.HTTP_201_CREATED)
        except Users.DoesNotExist:
            return Response("User not found", status=status.HTTP_404_NOT_FOUND)
        except Books.DoesNotExist:
            return Response("Book not found", status=status.HTTP_404_NOT_FOUND)

# View para listar livros de um usuário
class UserBooksView(APIView):
    def get(self, request, id_user):
        # Obtém todos os livros associados ao usuário
        user_books = UserBooks.objects.filter(id_user=id_user)
        # Retorna os livros associados ao usuário
        serializer = UsersBooksSerializers(user_books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
