from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home , name = 'home'),
    path('add/<str:params>', views.add , name = 'add' ),
    path('edit/<str:params>/<str:name>' , views.edit , name = 'edit')
]
