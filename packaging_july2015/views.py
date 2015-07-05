from django.shortcuts import render_to_response

from packaging_july2015.apps.kittens.models import Kitten

def index_view(request, *args, **context):
    context['kitten_count'] = Kitten.objects.count()
    return render_to_response('index.html', context)
