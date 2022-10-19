from django.urls import path
from post import views

app_name = 'post'

urlpatterns = [
    path('post/', views.Post_search, name='post_search'),
    path('comment/delete/<int:pk>/', views.comment_delete, name='delete'),
    path('comment/<int:id>/', views.create_comment, name= 'create_comment'), 
    path('edit/<int:id>/', views.edit, name = 'comment_edit'),
]
