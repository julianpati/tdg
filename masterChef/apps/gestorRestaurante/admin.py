from django.contrib import admin

# Register your models here.
from models import usuario, inventario, plato, ingrediente, menu, menu_platos, orden,descripcion_orden



# Register your models here.
admin.site.register(usuario)
admin.site.register(inventario)
admin.site.register(plato)
admin.site.register(ingrediente)
admin.site.register(menu)
admin.site.register(menu_platos)
admin.site.register(orden)
admin.site.register(descripcion_orden)