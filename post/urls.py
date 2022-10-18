from django.urls import path
from post import views

app_name = 'post'

urlpatterns = [
    path('post/', views.Post_search, name='post_search'),
    path('delete/<int:id>', views.Comment_delete, name='delete'),
    #path('', views.index, name=index),
    path('comment/', views.create_comment, name= 'create_comment'),
    #path('<int:pk>/edit/', views.edit, name = 'edit'),

]
