from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from . models import Product


def index(request):
    products = Product.objects.all()

    # Let's paginate
    paginator = Paginator(products, 9)
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context_dict = {
        'page_title': "Products",
        'page_sub_title': "",
        'products': products,
        'navbar': "products"
    }

    return render(request, 'products/products.html', context_dict)