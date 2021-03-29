from django.http import request
from django.shortcuts import render
from django.urls.base import reverse_lazy

from .forms import ProductForm, RawProductForm
from .models import Product

from django.views.generic import CreateView
from django.urls import reverse

# function based view
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        # after form is save render new form
        form = ProductForm()

    return render(request, "products/create.html", {'form': form})


# class based view
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/create1.html'
    # after the form is submitted you need to redirect to somewhere else
    # Let's redirect to new form
    def get_success_url(self):
        return reverse('products:create1')


# html template scratch
def custom_form(request):
    # get title from form
    if request.method == "POST":
        title = request.POST["title"]
        print(title)
    return render(request, 'products/input.html', {})


def custom_raw_form(request):
    form = RawProductForm()
    if request.method == 'POST':
        form = RawProductForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # we can store to our model if needed
            # like this
            # Product.objects.create(**form.cleaned_data)
        else:
            print(form.errors)

    return render(request, 'products/input1.html', {'form': form})
