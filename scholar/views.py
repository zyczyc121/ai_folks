from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from scholar.models import Scholar

def index(request):
    return HttpResponse("Scholar Index Here")
# Create your views here.


def field_rank(request, field = 'Data mining'):
    context = {'scholars': Scholar.objects.filter(classification = field)}
    return render(request, 'scholar/list.html', context)

def tag_search(request, tag_name):
    context = {'scholars': Scholar.objects.filter(tag__title__startswith = tag_name)}
    return render(request, 'scholar/list.html', context)

def profile(request, scholar_pk):
    scholar = get_object_or_404(Scholar, id = scholar_pk)
    return render(request, "scholar/index.html", {
        'scholar': scholar,    
    })
