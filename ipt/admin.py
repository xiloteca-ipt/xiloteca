from django.contrib import admin

# Register your models here.
from.models import Category, Color, Madeira,MadeirasAttribute, Banner

admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Madeira)
admin.site.register(MadeirasAttribute)
admin.site.register(Banner)
