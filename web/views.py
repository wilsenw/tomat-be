import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import Product


# Create your views here.
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


class ProductListView(ListView):
    model = Product
    template_name = "about.html"
