from django.urls import path

from . import views

urlpatterns = [
    path('list', views.index, name='index'),
    path('detail/<id>', views.detail, name='detail'),
    path('create', views.create, name='create'),
    path('edit/<id>', views.edit, name='edit'),
    path('delete/<id>', views.delete, name='delete'),
]