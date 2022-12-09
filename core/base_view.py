from django.shortcuts import render
from manufacturing.models import Product


def base_view(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        if search:
            products = Product.objects.filter(title__icontains=search)
            if products:
                data = {
                    'products': products
                }
                return render(request, 'product/search.html', context=data)
            return render(request, 'errors/404_page_not_foud.html')
    return render(request, 'errors/404_page_not_foud.html')
