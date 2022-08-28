from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from mainapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url="mainapp/")),
    path("mainapp/", include("mainapp.urls")),
]
