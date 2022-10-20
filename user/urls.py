from xml.etree.ElementInclude import include
from django.urls import path,include
from django.contrib.auth import views as auth_views
from user import views


app_name = 'user'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    
    # 221020 최해민 search 추가
    path('upload/', views.upload, name='upload'),


]


