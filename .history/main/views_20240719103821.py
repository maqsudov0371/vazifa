from django.shortcuts import render


def blogs(request):
    cars = [
        {'id': 1 ,'name': 'BMW M5 E60', 'color': 'black', 'year': '2010'},
        {'id': 2, 'name': 'Mercedes-Benz S-Class', 'color': 'white', 'year': '2020'},
        {'id': 3, 'name': 'Toyota Camry', 'color': 'red', 'year': '2015'},
        {'id': 4, 'name': 'Honda Accord', 'color': 'blue', 'year': '2018'},       
        ]
    context = {
        'list':'Mashinalar royhati',
        'cars': cars
    }
    return render(request, 'blog.html', context)


def blog_detail(request):
    companys = [
        {'id': 1, 'name': 'Tesla', 'year': '2003', 'popular': 'cars'},
        {'id': 2, 'name': 'Google', 'year': '1998', 'popular': 'search engine'},
        {'id': 3, 'name': 'Facebook', 'year': '2004', 'popular': 'social media'},
        {'id': 4, 'name': 'Instagram', 'year': '2010', 'popular': 'photo sharing'}
    
    ]
    context = {
        'list2':'Kompaniyalar royxati',
        'companys': companys
    }
    return render(request, 'blog.html', context)


def comment_create(request):
    context = {
        'list3':'Dasturlash turlari'
    }
    return render(request, 'login.html', context)

