from django.urls import path 
from . import views

app_name = "post"

urlpatterns = [
    path('post/', views.Post_search, name='post_search'),
    path('delete/<int:id>', views.comment_delete, name='delete')
]
