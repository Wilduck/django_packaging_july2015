from django.shortcuts import render_to_response


def index_view(request, *args, **kwargs):
    return render_to_response('index.html', kwargs)
