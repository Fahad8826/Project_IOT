from  django.urls import path

from myapp.views import UserCreate, UserReadUpdate

# from myapp.views import home

urlpatterns =[

    path('create',UserCreate.as_view(),name='create'),
    path('read/',UserReadUpdate.as_view(),name='read'),
]