from django.urls import path

from landing.views import TemplView

app_name = 'landing'

urlpatterns = [
    path('landing/', TemplView.as_view(), name='landing'),
]