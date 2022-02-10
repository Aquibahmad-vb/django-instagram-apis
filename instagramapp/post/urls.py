
from django.urls import path
from . import views

urlpatterns=[
    # path('',views.getRoute),
    path('post/',views.getPost),
    path('post/<str:pk>/',views.PostDetails)
]