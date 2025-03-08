from django.contrib import admin
from apps.settings.models import Product, ProductImage, Category
from django.utils.html import format_html
from mptt.admin import DraggableMPTTAdmin

# Register your models here.

class ProductImageAdmin(admin.TabularInline):
    model = ProductImage
    extra = 1
    readonly_fields = ['image_tag']
    
    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height="50px" />'.format(obj.image.url))
    
    image_tag.short_description = "Изображение"
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('title', 'description', 'price', 'is_active', 'created_at', 'manufacture', 'amount', 'brand', 'guarantee', 'article')
    list_editable=['is_active']
    readonly_fields = ('created_at',)
    fieldsets = (
        (None, {'fields': (
            'title',
            'description',
            'price',
            'is_active',
            'created_at',
            'manufacture',
            'amount',
            'brand',
            'guarantee',
            'article',

        )}),
    )
    
    inlines = [ProductImageAdmin]
    
    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height="30px" />'.format(obj.get_first_image()))

    image_tag.short_description = 'Изображение'

    
@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count', )
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'
