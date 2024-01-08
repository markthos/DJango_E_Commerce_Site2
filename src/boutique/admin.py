from django.contrib import admin
from oscar.core.loading import get_model

Boutique = get_model('boutique', 'Boutique')

# Register your models here.

class BoutiqueAdmin(admin.ModelAdmin):
    pass

admin.site.register(Boutique, BoutiqueAdmin)
