from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse(' <a href="about" >О нас</a>')

def about(request):
    return render(request, 'about.html', {'greeting': 'hello', 'goodbye': 'bye'})

def test(request):
    return render(request, 'test.html', {'greeting': 'HeLlo Mister Bin!', 'goodbye': 'ByE', 'list': [1, 2, 3, 'привет'],
                                         'value': ['45', 5, 6], 'size_file': 1, 'athlete_list': ['Вася', 'Артём']})
