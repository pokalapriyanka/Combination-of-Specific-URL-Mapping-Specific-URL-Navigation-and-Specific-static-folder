from django.shortcuts import render

# Create your views here.
def food(request):
    return render(request,'food.html')
def drinks(request):
    return render(request,'drinks.html')