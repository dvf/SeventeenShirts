from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.contrib import messages

from . models import Product
from . forms import BuyShirtForm


def index(request):
    products = Product.objects.all()

    # Let's paginate
    paginator = Paginator(products, 10)
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

    return render(request, 'shop/products/index.html', context_dict)


def detail(request, product_id):
    if request.method == 'POST':
        form = BuyShirtForm(request.POST)

        if form.is_valid():
            # Create a new purchase order

            messages.success(request, "Thank you! Your product has been purchased.")
            return redirect('shop:index')
    else:
        form = BuyShirtForm()

    context_dict = {
        'page_title': "Viewing Product" + product_id,
        'product': Product.objects.get(pk=product_id),
        'navbar': "products",
        'form': form
    }

    return render(request, 'shop/products/detail.html', context_dict)