
from django.views.generic.base import RedirectView
from django.urls import path

from . import views

urlpatterns = [
    path("", RedirectView.as_view(url="/static/rocksite/login/index.html"), name="login"),
    path("search", views.search, name="search"),
]