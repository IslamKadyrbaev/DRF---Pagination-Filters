from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.users.views import UserAPIList, UserAPIRegister

router = DefaultRouter()
router.register(f'list_user', UserAPIList, basename='user_list')
router.register(f'create-user', UserAPIRegister, basename='create_user')

urlpatterns = [
    
]
urlpatterns+=router.urls