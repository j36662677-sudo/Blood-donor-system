from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_donor, name='add_donor'),
    path('', views.donor_list, name='donor_list'),
    path('search/', views.search_donors, name='search_donors'),
    path('<int:donor_id>/edit/', views.edit_donor, name='edit_donor'),
    path(
    '<int:donor_id>/delete/',
    views.delete_donor,
    name='delete_donor'
),
]