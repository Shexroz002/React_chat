from django.urls import path,re_path
from .views import RegisterView,UserListApiView,UserInfoApiView
from rest_framework.authtoken import views as auth_views

urlpatterns =[
    path('api/register',RegisterView.as_view(),name='register'),
    path('api/user/list',UserListApiView.as_view(),name='userlist'),
    path('api/user/info/<int:id>',UserInfoApiView.as_view(),name='userinfo'),
    re_path(r'^auth/$', auth_views.obtain_auth_token),

]
