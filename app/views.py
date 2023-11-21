from django.shortcuts import render

# Create your views here.
def forloop(request):
    d = {'name':'ravi mahto'}
    return render(request,'for_loop.html',d)