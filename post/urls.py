from nturl2path import url2pathname
from django.urls import path, include
from post import views

app_name = 'post'

urlpatterns = [
    #path('', views.index, name=index),
    path('comment/', views.create_comment, name= 'create_comment'), 
    #path('<int:pk>/edit/', views.edit, name = 'edit'),

]
