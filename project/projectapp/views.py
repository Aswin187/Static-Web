from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import team


# Create your views here.
def demo(request):
    obj = place.objects.all()
    obj1 = team.objects.all()
    return render(request, "index.html", {'result': obj, 'res': obj1})

#
# def addition(request):
#     ob=place.objects.all()
#     return render(request,"index.html",{'res':ob})


# def addition(request):
#     x =int( request.GET['num1'])
#     y =int( request.GET['num2'])
#     res = x + y
#     return render(request, 'about.html', {'result': res})
