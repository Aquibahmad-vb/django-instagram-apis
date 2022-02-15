from django.urls import path
from . import views

urlpatterns=[
    # path('',views.getRoute),
    path('user/',views.getUser),
    path('user/<str:pk>/',views.userDetails),
    path('login/',views.login),
    path('changepassword/<str:pk>/',views.changePassword)
]