from rest_framework.routers import DefaultRouter
from apps.settings.views import ProductMixins

router=DefaultRouter()

router.register(r'products', ProductMixins, basename='product')

urlpatterns = router.urls
