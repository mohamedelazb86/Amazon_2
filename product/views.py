from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Product,Review,ProductImage,Brand

class Product_List(ListView):
    model=Product
    template_name='product/product_list.html'
    paginate_by=24

class Product_Detail(DetailView):
    model=Product
    template_name='product/product_detail.html'

    
    

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product=self.get_object())
        context["images"] = ProductImage.objects.filter(product=self.get_object())
        return context

class Brand_List(ListView):
    model=Brand
    template_name='product/brand_list.html'
    paginate_by=25

class Brand_Detail(DetailView):
    model=Brand
    template_name='product/product_detail.html'
    

