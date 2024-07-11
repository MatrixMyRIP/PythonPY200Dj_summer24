from django.urls import path

from app_new.views import MyT
from django.views.generic import TemplateView

urlpatterns = [
    # path('', my_view),
    # path('', my_view),
    # path('', MyT.as_view()),
    path('', TemplateView.as_view(template_name="hello.html",
                                  extra_context={"var": 10,
                                                   "list": [1,2,3,4,5]})),
]