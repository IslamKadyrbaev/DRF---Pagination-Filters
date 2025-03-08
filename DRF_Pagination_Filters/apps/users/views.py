from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated


from apps.users.models import User
from apps.users.serializer import UserSerializer, UserRegisterSerializer

# Create your views here.

class UserAPIList(GenericViewSet,
                mixins.ListModelMixin):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[IsAuthenticated]

class UserAPIRegister(GenericViewSet,
                mixins.CreateModelMixin):
    queryset=User.objects.all()
    serializer_class=UserRegisterSerializer

# class UserMixins(GenericViewSet,
#                     mixins.CreateModelMixin, 
#                     mixins.ListModelMixin, 
#                     mixins.UpdateModelMixin, 
#                     mixins.DestroyModelMixin):
#     queryset=User.objects.all()
#     serializer_class=UserRegisterSerializer

#     def create(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)
#     def list(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
#     def destroy(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)
#     def update(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)  