from django.urls import path
from . import views


urlpatterns = [path('', views.APIList.as_view()), path(
    '<int:pk>/', views.APIDetail.as_view()), ]
