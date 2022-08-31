from django.urls import path

from api import views

urlpatterns = [
  path('resume/', views.ProfileView.as_view(), name='resume'),
  path('resume/<int:pk>', views.ProfileView.as_view(), name='list')
]