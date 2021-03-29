from django.urls import path
from .views import product_create_view, ProductCreateView, custom_form, custom_raw_form


app_name = 'products'

urlpatterns = [
    path('create/', product_create_view, name="create"),
    path('create1/', ProductCreateView.as_view(), name='create1'),
    path('input/', custom_form, name='input'),
    path('input1/', custom_raw_form, name='input1'),
]
