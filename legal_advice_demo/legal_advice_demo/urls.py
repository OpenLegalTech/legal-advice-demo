from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include
from django.urls import path

urlpatterns = [
    path('', include('legal_advice_builder.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls)
]
