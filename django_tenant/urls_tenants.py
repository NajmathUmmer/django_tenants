
from django.contrib import admin
from django.urls import path, include
from myapp.views import Home, List, SignUp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home.as_view(),name='home'),
    path('list/',List.as_view(),name = 'list'),
    path('signup/', SignUp.as_view(), name='signup'),
]
