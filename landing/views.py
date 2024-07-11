from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .forms import TemplateForm


def ip_user(request):
    user_agent = request.META.get('HTTP_USER_AGENT')
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # Получение IP
    else:
        ip = request.META.get('REMOTE_ADDR')  # Получение IP



class TemplView(View):
    def get(self, request):
        return render(request, 'landing/index.html')

    # TODO скопируйте код, что есть в template_view в теле условия request.method == "GET"
    def post(self, request):
        received_data = request.POST  # Приняли данные в словарь
        form = TemplateForm(received_data)
        print(form)
        if form.is_valid():
            return JsonResponse(data=form.cleaned_data, json_dumps_params={"indent": 4, "ensure_ascii": False})
        return render(request, 'landing/index.html', context={"form": form})
