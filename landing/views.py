from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import FormView

from .forms import TemplateForm


# class TemplView(View):
#     def get(self, request):
#         return render(request, 'landing/index.html')
#
#     # TODO скопируйте код, что есть в template_view в теле условия request.method == "GET"
#     def post(self, request):
#         received_data = request.POST  # Приняли данные в словарь
#         form = TemplateForm(received_data)
#         print(form)
#         if form.is_valid():
#             my_text = form.cleaned_data.get(
#                 "my_text")
#             my_email = form.cleaned_data.get("my_email")
#             my_message = form.cleaned_data.get("my_message")
#             x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#             if x_forwarded_for:
#                 ip = x_forwarded_for.split(',')[0]  # Получение IP
#             else:
#                 ip = request.META.get('REMOTE_ADDR')  # Получение IP
#
#             user_agent = request.META.get('HTTP_USER_AGENT')
#
#             return JsonResponse(data={"my_text": my_text,
#                                       "my_email": my_email,
#                                       "my_message": my_message,
#                                       "ip": ip,
#                                       "user_agent": user_agent},
#                                 json_dumps_params={"indent": 4, "ensure_ascii": False})
#         return render(request, 'landing/index.html', context={"form": form})


class MyFormView(FormView):
    template_name = 'landing/index.html'
    form_class = TemplateForm
    success_url = '/'

    def form_valid(self, form):
        def client_ip():
            request = self.request
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]  # Получение IP
            else:
                ip = request.META.get('REMOTE_ADDR')  # Получение IP

            user_agent = request.META.get('HTTP_USER_AGENT')
            return {"ip": ip, "user_agent": user_agent}

        new_form = form.cleaned_data
        client_info = client_ip()
        new_form.update(client_info)

        return JsonResponse(data=new_form,
                            json_dumps_params={"indent": 4,
                                               "ensure_ascii": False})
