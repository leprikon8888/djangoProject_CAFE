from django.urls import path
from .views import menu, menu_dish, menu_category

app_name = 'menu'

urlpatterns = [
    path('', menu, name='menu'),
    path('<int:category>', menu_category, name='menu_category'),
    path('<int:category>/<int:dish>', menu_dish, name='menu_dish'),
]