from django.shortcuts import render, redirect, get_object_or_404

from phones.models import Phone


def index(request):
    return redirect("catalog")


def show_catalog(request):
    phones = Phone.objects.all()

    # Определяем параметры сортировки из GET запроса
    sort_by = request.GET.get("sort")
    if sort_by == "name":
        phones = phones.order_by("name")
    elif sort_by == "max_price":
        phones = phones.order_by("-price")
    elif sort_by == "min_price":
        phones = phones.order_by("price")

    context = {"phones": phones}
    template = "catalog.html"
    return render(request, template, context)


def show_product(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    template = "product.html"
    context = {"phone": phone}
    return render(request, template, context)
