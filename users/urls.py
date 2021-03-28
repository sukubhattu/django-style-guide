from django.urls import path
from .views import SignUpPageView, SignUpPageView1, SignUpPageView2

app_name = 'users'

urlpatterns = [
    path('signup/', SignUpPageView.as_view(), name="signUp"),
    path('signup1/', SignUpPageView1.as_view(), name="signUp1"),
    path('signup2/', SignUpPageView2.as_view(), name="signUp2"),
]
