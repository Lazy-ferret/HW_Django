from django.shortcuts import render, redirect
from operator import itemgetter

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones_object = Phone.objects.values()
    type_sorted = request.GET.get('sort')
    if type_sorted == 'min_price':
        phones_object = sorted(phones_object, key=itemgetter('price'))
    elif type_sorted == 'max_price':
        phones_object = sorted(phones_object, key=itemgetter('price'), reverse=True)
    elif type_sorted == 'name':
        phones_object = sorted(phones_object, key=itemgetter('name'))
    context = {
        'phones': phones_object
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones_object = Phone.objects.values()
    context = {}
    for phone in phones_object:
        if slug == phone['slug']:
            context['phone'] = phone
    return render(request, template, context)
