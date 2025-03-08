from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError('Телефонный номер обязательный')
        user=self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phone, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    phone=models.CharField(max_length=15, unique=True)
    first_name=models.CharField(max_length=50, blank=True, null=True)
    last_name=models.CharField(max_length=50, blank=True, null=True)
    is_active=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)

    objects=UserManager()

    USERNAME_FIELD='phone'
    REQUIRED_FIELDS=[]

    def __str__(self):
        return self.phone
    
    class Meta:
        verbose_name='Пользователь'
        verbose_name_plural='Пользователи'

# # Фильтры для категорий
# class CategoryFilter(filters.FilterSet):
#     name = filters.CharFilter(lookup_expr='icontains')
#     created_at = filters.DateFromToRangeFilter()
    
#     class Meta:
#         model = Category
#         fields = ['name', 'created_at']
