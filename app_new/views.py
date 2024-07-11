from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class MyT(TemplateView):
    template_name = "hello.html"
    extra_context = {"var": 10, "list": [1, 2, 3, 4, 5]}
