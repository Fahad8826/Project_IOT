from  django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from myapp import views
from myapp.views import *

# from myapp.views import home

urlpatterns =[
    path('create',UserCreate.as_view(),name='create'),
    path('read/',UserReadUpdate.as_view(),name='read'),
    path('delete/<int:pk>/',UserDelete.as_view(),name ='delete'),
    path('update/<int:pk>',UserUpdate.as_view(),name='update'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),  # JWT Login
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]