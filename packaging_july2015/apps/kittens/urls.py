from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^random/', views.random_kitten_view, name='random-kitten'),
]
