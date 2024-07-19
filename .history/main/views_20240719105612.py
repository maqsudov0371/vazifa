from django.shortcuts import render


def blogs(request):
    cars = [
        {'id': 1 ,'name': 'BMW M5 E60', 'color': 'black', 'year': '2010'},
        {'id': 2, 'name': 'Mercedes-Benz S-Class', 'color': 'white', 'year': '2020'},
        {'id': 3, 'name': 'Toyota Camry', 'color': 'red', 'year': '2015'},
        {'id': 4, 'name': 'Honda Accord', 'color': 'blue', 'year': '2018'},  
        {'id': 5, 'name': 'Audi A6', 'color': 'silver', 'year': '2012'},
        {'id': 6, 'name': 'Nissan GT-R', 'color': 'green', 'year': '2018'},
        {'id': 7, 'name': 'Volkswagen Beetle', 'color': 'gray', 'year': '2015'},
        {'id': 8, 'name': 'Ford Mustang', 'color': 'white', 'year': '2017'},
        {'id': 9, 'name': 'Hyundai Sonata', 'color': 'blue', 'year': '2016'},
        {'id': 10, 'name': 'BMW 3 Series', 'color': 'black', 'year': '2019'},
        {'id': 11, 'name': 'Ford F-150', 'color': 'blue', 'year': '2018'},
        {'id': 12, 'name': 'Ford Fusion', 'color': 'red', 'year': '2018'},
        {'id': 13, 'name': 'Chevrolet Corvette', 'color': 'blue', 'year': '2015'},
        {'id': 14, 'name': 'Toyota Highlander', 'color': 'green', 'year': '2017'},

        ]
    context = {
        'list':'Mashinalar royhati',
        'cars': cars
    }
    return render(request, 'blog.html', context)


def register(request):
    companys = [
        {'id': 1, 'name': 'Tesla', 'year': '2003', 'popular': 'cars'},
        {'id': 2, 'name': 'Google', 'year': '1998', 'popular': 'search engine'},
        {'id': 3, 'name': 'Facebook', 'year': '2004', 'popular': 'social media'},
        {'id': 4, 'name': 'Instagram', 'year': '2010', 'popular': 'photo sharing'},
        {'id': 5, 'name': 'Amazon', 'year': '1994', 'popular': 'e-commerce'},
        {'id': 6, 'name': 'Netflix', 'year': '1997', 'popular': 'movies'},
        {'id': 7, 'name': 'YouTube', 'year': '2005', 'popular': 'video sharing'},
        {'id': 8, 'name': 'Apple', 'year': '2009', 'popular': 'phone'},
        {'id': 9, 'name': 'Microsoft', 'year': '1975', 'popular': 'software'},
        {'id': 10, 'name': 'Twitter', 'year': '2006', 'popular': 'social media'},
        {'id': 11, 'name': 'Pinterest', 'year': '2010', 'popular': 'social media'},

    
    ]
    context = {
        'list2':'Kompaniyalar royxati',
        'companys': companys
    }
    return render(request, 'register.html', context)


def login(request):
    programming = [
        {'id': 1, 'name': 'Python', 'creator':'Guido van Rossum', 'year': '1991'}
        {'id': 2, 'name': 'Java', 'creator':'James Gosling', 'year': '1995'},
        {'id': 3, 'name': 'C++', 'creator':'Bjarne Stroustrup', 'year': '1985'},
        {'id': 4, 'name': 'C#', 'creator':'Scott Meyers', 'year': '2000'},
        {'id': 5
    ]
    context = {
        'list3':'Dasturlash turlari'
    }
    return render(request, 'login.html', context)

