from  django.urls import path

from myapp.views import UserCreate, UserReadUpdate, UserDelete

# from myapp.views import home

urlpatterns =[
    path('create',UserCreate.as_view(),name='create'),
    path('read/<int:pk>/',UserReadUpdate.as_view(),name='read'),
    path('delete/<int:pk>/',UserDelete.as_view(),name ='delete'),
]