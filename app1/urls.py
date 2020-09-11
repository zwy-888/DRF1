
from django.urls import path

from app1 import views

urlpatterns = [
    path('a/', views.a),
    # 类视图需要在后面加.as_view()
    path('app/', views.UserView.as_view()),
    # 匹配包含参数的路由
    path('api/', views.Api.as_view()),
    path('api/<str:id>/', views.Api.as_view()),
    # rsf视图
    path('API/', views.UserAPIView.as_view()),
    path('API/<str:id>/', views.UserAPIView.as_view()),
]
