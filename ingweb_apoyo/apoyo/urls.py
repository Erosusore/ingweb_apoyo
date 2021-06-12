from django.urls import path
from .views import home, poblar_bd, producto

urlpatterns = [
    path('', home, name="home"),
    path('poblar_bd', poblar_bd, name="poblar_bd"),
    path('producto/<action>/<id>', producto, name="producto")
]
