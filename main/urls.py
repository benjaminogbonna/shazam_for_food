from django.urls import path
from .views import index, camera


urlpatterns = [
    path('', index, name='index'),
    path('c', camera, name='c')
]
