from django.contrib import admin
from .models import MenuCategory, MenuDish


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(MenuDish)
class MenuDishAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


