from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm, CustomUserCreationForm1


class SignUpPageView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('pages:index')
    extra_context = {'title': 'Default django'}
    template_name = "users/registration.html"


class SignUpPageView1(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('pages:index')
    extra_context = {'title': 'Sign up with crispy'}
    template_name = "users/registration1.html"


class SignUpPageView2(CreateView):
    form_class = CustomUserCreationForm1
    success_url = reverse_lazy('pages:index')
    extra_context = {'title': 'Sign up with custom'}
    template_name = "users/registration2.html"