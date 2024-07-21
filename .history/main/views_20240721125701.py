from django.shortcuts import render


def products(request):
    person = [
        {img}
    ]
    return render(request, 'product.html')

