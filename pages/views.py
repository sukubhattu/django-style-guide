# Import CBV template view
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "pages/index.html"
