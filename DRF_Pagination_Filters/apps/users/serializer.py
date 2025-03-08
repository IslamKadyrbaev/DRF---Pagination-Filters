from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id', 'phone', 'first_name', 'last_name']

class UserRegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=20, write_only=True)
    confirm_password=serializers.CharField(max_length=20, write_only=True)

    class Meta:
        model = User
        fields=['id', 'phone', 'first_name', 'last_name', 'password', 'confirm_password']

    def validate(self, attrs):
        if attrs['password'] !=attrs['confirm_password']:
            raise serializers.ValidationError({'confirm_password': 'Пароли не совпадают'})
        if len(attrs['password'])<8:
            raise serializers.ValidationError({'password': 'не менее 8 символов'})
        
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user=User.objects.create(
            phone=validated_data['phone'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
        
        

