from django.conf.urls import url
from django.urls import path, include


from . import views

urlpatterns = [
    path('', views.LocationListView.as_view(), name='list'),
    path('create/', views.LocationCreateView.as_view(), name='create'),
    path('<int:pk>/', views.LocationDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.LocationUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.LocationDeleteView.as_view(), name='delete')
]
