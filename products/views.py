from django.shortcuts import render

# Create your views here.

def base_view(request):
    return render(request, "base.html")

def product_list(request):
    return render(request, 'это Лист продуктов')