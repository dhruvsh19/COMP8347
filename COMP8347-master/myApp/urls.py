from django.urls import path
from myApp import views


app_name = 'myApp'

urlpatterns = [
    path(r'login', views.user_login, name='user_login'),
    path(r'logout', views.user_logout, name='user_logout'),
    path(r'myaccount', views.myaccount, name='myaccount'),
    path(r'', views.index, name='index'),
    path('about', views.about, name='about'),
    path(r'detail/<int:top_no>/', views.detail, name='detail'),
    path(r'courses/<int:cour_id>', views.coursedetail, name='coursedetail'),
    path(r'courses', views.courses, name='courses'),
    path(r'place_order', views.place_order, name='place_order'),
]
