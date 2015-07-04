from django.shortcuts import render_to_response


def random_kitten_view(request, *args, **kwargs):
    return render_to_response("kittens/random.html", kwargs)
