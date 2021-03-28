from django.urls import path

app_name = 'pages'

from .views import HomePage

urlpatterns = [path('', HomePage.as_view(), name='index')]
