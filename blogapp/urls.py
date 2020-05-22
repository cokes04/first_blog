from django.conf.urls import url
from django.urls import path
from  . import views
app_name ="blogapp"
urlpatterns =[
    path('',views.post_list,name="post_list"),
    path('post/<int:pk>/', views.post_detail, name="post_detail"),
    path('post/new/', views.post_new, name="post_new"),
    path('post/<int:pk>/edit/', views.post_edit, name="post_edit"),
    path('post/management/', views.post_management, name="post_management"),
]