from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('thesis/', views.Thesis.as_view(), name="thesis"),
    path('aboutme/', views.Aboutme.as_view(), name="aboutme"),
    path('myjourney/', views.Myjourney.as_view(), name="myjourney"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    
]