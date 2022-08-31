from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["news_title"] = "Громкий новостной заголовок"
        context["news_preview"] = "Предварительное описание, которое заинтересует каждого"
        context["range"] = range(5)
        context["data_obj"] = datetime.now()
        return context

class CoursesPageView(TemplateView):
    template_name = "mainapp/courses.html"


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"
