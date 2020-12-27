from django.http import Http404
from django.shortcuts import render
from .models import MyData


# Create your views here.

def index(request):
    my_data_obj = MyData.objects.all()
    context = {'my_data_obj': my_data_obj,}
    return render(request, 'app1/index.html', context)


def detail(request, nom):

    try:
        user_info = MyData.object.filter(nom=nom)
    except MyData.DoesNotExist:
        raise Http404("Nom does not exist")

    return render(request, 'app1/detail.html', {'user_info': user_info})
