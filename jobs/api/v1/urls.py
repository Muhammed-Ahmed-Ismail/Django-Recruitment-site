from django.urls import path

from jobs.api.v1.views import index, detail, create, edit, delete, apply, assign,my_jobs

urlpatterns = [
    path('list', index, name='index'),
    path('myjobs', my_jobs, name='index'),
    path('detail/<int:job_id>', detail, name='detail'),
    path('create', create, name='create'),
    path('edit/<int:job_id>', edit, name='edit'),
    path('delete/<int:job_id>', delete, name='delete'),
    path('apply/<int:job_id>', apply, name='apply'),
    path('assign/<int:job_id>/developer/<int:dev_id>', assign, name='apply')
]
