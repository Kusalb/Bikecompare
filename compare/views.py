from django.core.serializers import json
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from compare.models import CompareBikeList


def index(request):
    compare = CompareBikeList.objects.all()
    print(compare)
    return render(request, 'compare/index.html', context={'compare': compare})

#
# def search_titles(request):
#     if request.method == "POST":
#         search_text = request.POST['search_text']
#     else:
#         search_text = ''
#     compare = CompareBikeList.objects.filter(bname__contains=search_text)
#     return render(request, 'compare/ajax_search.html', {'compare': compare})

def search_titles(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
    else:
        search_text = ''
    autosearch = CompareBikeList.objects.filter(bname__contains=search_text)
    return render(request, 'compare/ajax_search.html', {'autosearch': autosearch})

    return None