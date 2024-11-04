from django.shortcuts import render

def home(request):
    return render(request, 'recipes/home.html')

def recipe1(request):
    return render(request, 'recipes/recipe1.html')

def recipe2(request):
    return render(request, 'recipes/recipe2.html')

def recipe3(request):
    return render(request, 'recipes/recipe3.html')

def recipe4(request):
    return render(request, 'recipes/recipe4.html')

def recipe5(request):
    return render(request, 'recipes/recipe5.html')
