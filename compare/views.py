from django.core.serializers import json
from django.shortcuts import render, render_to_response

# Create your views here.
from django.http import HttpResponse
from django.template.context_processors import csrf

from compare.models import CompareBikeList
from django.views.decorators.csrf import csrf_exempt


def index(request):
    args = {}
    args.update(csrf(request))
    return render(request, 'compare/index.html', args)


#
# def search_titles(request):
#     if request.method == "POST":
#         search_text = request.POST['search_text']
#     else:
#         search_text = ''
#     compare = CompareBikeList.objects.filter(bname__contains=search_text)
#     return render(request, 'compare/ajax_search.html', {'compare': compare})

@csrf_exempt
def search_titles(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
        print(search_text)
    else:
        search_text = ''
    autosearch = CompareBikeList.objects.filter(bname__contains=search_text)
    print(autosearch)
    return render_to_response('compare/ajax_search.html', {'autosearch': autosearch})


