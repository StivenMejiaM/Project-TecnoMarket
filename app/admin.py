from django.contrib import admin
from .models import Marca, Producto, Contacto, ImagenProduct0
from .forms import ProductoForm

# Register your models here.
class ImagenProductoAdmin(admin.TabularInline):
    model = ImagenProduct0




class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre","precio","nuevo","marca"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_filter = ["marca", "nuevo"]
    list_per_page = 5
    form = ProductoForm
    inlines = [
        ImagenProductoAdmin
    ]


admin.site.register(Marca)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Contacto)