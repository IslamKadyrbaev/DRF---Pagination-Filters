from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


from apps.settings.models import Product
from apps.settings.serializer import ProductSerializer
from apps.settings.pagination import ProductPagination

class ProductMixins(GenericViewSet,
                    mixins.CreateModelMixin, 
                    mixins.ListModelMixin, 
                    mixins.UpdateModelMixin, 
                    mixins.DestroyModelMixin):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    pagination_class=ProductPagination

    filter_backends=[DjangoFilterBackend, SearchFilter, OrderingFilter]

    search_fields=['title', 'description']
    ordering_fields=['price', 'created_at']
    ordering=['-created_at']

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)    
    
