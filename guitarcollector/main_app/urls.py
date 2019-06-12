from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('guitars/', views.guitars_index, name='guitar'),
  path('guitars/<int:guitar_id>/', views.guitars_detail, name='detail'),
  path('guitars/create/', views.GuitarCreate.as_view(), name='guitars_create'),
  path('guitars/<int:pk>/update/', views.GuitarUpdate.as_view(), name='guitars_update'),
  path('guitars/<int:pk>/delete/', views.GuitarDelete.as_view(), name='guitars_delete'),
  path('guitars/<int:guitar_id>/add_maintenance/', views.add_maintenance, name='add_maintenance'),
]