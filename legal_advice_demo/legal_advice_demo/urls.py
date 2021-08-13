from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path('', include('legal_advice_builder.urls')),
    path('admin/', admin.site.urls)
]
