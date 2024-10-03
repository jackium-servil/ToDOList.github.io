from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name='home',),
    path("edit/<int:pk>", views.edit, name='edit'),
    path('deleting/<int:pk>', views.deleting, name='deleting'),
    path('views/<int:pk>', views.viewing, name='view'), 
]
