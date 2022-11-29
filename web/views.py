from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Catalogue
from .forms import CatalogueForm


def catalogueView(request):
    catalogues = Catalogue.objects.all()
    # paginator = Paginator(catalogues, 2)
    # page_number = request.GET.get('page')
    # print(page_number)
    # page_obj = paginator.get_page(page_number)
    return render(request, 'catalogue.html', {'catalogues': catalogues})
