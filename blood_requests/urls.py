
from django.urls import path
from . import views

urlpatterns = [
    path('', views.request_list, name='request_list'),
    path('create/', views.create_request, name='create_request'),
    path('<int:request_id>/update-status/', views.update_status, name='update_status'),
]
