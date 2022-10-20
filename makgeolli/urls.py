from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
from makgeolli import views
app_name = 'makgeolli'
urlpatterns = [
    # 221018 최해민 Makgeolli url 추가
    path('makgeolli/', views.makgeolli, name='makgeolli'),
    path('makgeolli/<int:id>', views.makgeolli_detail, name='detail'),


]
