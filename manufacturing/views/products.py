from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from manufacturing.forms.products import ProductForm
from manufacturing.models import Product, Category

'''
def home_page(request):
    products = Product.objects.all()
    data = {
        'products': products
    }
    return render(request, 'product/product_list.html', data)
'''


class HomePageView(ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'


# def product_detail(request, pk):
#     product = Product.objects.get(id=pk)
#     data = {
#         'product': product
#     }
#     return render(request, 'product/product_detail.html', data)


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product/product_create.html'
    form_class = ProductForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.pk
        return super().form_valid(form)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'
    context_object_name = 'product'


#
# def product_update(request, pk):
#     categories = Category.objects.all()
#     post = get_object_or_404(Product, id=pk)
#     data = {
#         'product': post,
#         'categories': categories
#     }
#     if request.method == 'POST':
#         form = ProductForm(request.POST, files=request.FILES)
#         product = Product.objects.get(id=pk)
#         if form.is_valid():
#             title = form.cleaned_data['title']
#             category = form.cleaned_data['category']
#             description = form.cleaned_data['description']
#             quantity = form.cleaned_data['quantity']
#             manufacturing_date = form.cleaned_data['manufacturing_date']
#             image = form.cleaned_data['image']
#             product.title = title
#             product.category_id = category
#             product.description = description
#             product.quantity = quantity
#             product.manufacturing_date = manufacturing_date
#             product.image = image
#             product.save()
#             return redirect('/')
#         return render(request, 'product/product_update.html', data)
#     return render(request, 'product/product_update.html', data)
#


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_update.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        ctx = super(ProductUpdateView, self).get_context_data(**kwargs)
        ctx['categories'] = Category.objects.all()
        return ctx


def product_delete(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('/')
