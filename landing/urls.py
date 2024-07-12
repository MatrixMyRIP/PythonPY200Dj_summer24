from django.urls import path

# from landing.views import TemplView
from landing.views import MyFormView

app_name = 'landing'

urlpatterns = [
    path('landing/', MyFormView.as_view(), name='landing'),
    # path('landing/', TemplView.as_view(), name='landing'),
]