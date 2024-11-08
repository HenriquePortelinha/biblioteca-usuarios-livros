from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from ..models import Users, Books, UserBooks

class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'  
        read_only_fields = ('created_at',)  

    def create(self, validated_data):
        
        password = validated_data.pop('user_password')
        
      
        user = Users.objects.create(**validated_data)
        
   
        user.user_password = make_password(password)
        
    
        user.save()
        
        return user

class BooksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'
        
class UsersBooksSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserBooks
        fields = '__all__'
        
        from django.contrib.auth.hashers import make_password

    def create(self, validated_data):
        password = validated_data.pop('user_password')
        user = Users.objects.create(**validated_data)
        user.user_password = make_password(password)
        user.save()
        return user
