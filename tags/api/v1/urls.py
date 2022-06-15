from django.urls import path

from tags.api.v1.views import index

urlpatterns = [
    path('list', index, name='index'),
    # path('detail/<int:job_id>', detail, name='detail'),
    # path('create', create, name='create'),
    # path('edit/<int:job_id>', edit, name='edit'),
    # path('delete/<int:job_id>', delete, name='delete'),
]
