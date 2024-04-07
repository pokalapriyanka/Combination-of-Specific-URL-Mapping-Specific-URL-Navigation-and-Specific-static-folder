from django.shortcuts import render

# Create your views here.
def clothes(request):
    return render(request,'clothes.html')
def shoes(request):
    return render(request,'shoes.html')