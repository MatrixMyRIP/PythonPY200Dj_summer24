from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import TemplateView, FormView

from .models import get_random_text
from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect
from django.contrib.auth import login, logout, authenticate
from .forms import TemplateForm, AuthenticationForm, CustomUserCreationForm
from django.views import View


# def template_view(request):
#     if request.method == "GET":
#         return render(request, 'app/template_form.html')
#
#     if request.method == "POST":
#         received_data = request.POST  # Приняли данные в словарь
#         print(received_data)
#
#         # как пример получение данных по ключу `my_text`
#         # my_text = received_data.get('my_text')
#         return JsonResponse(data={
#             "my_text": received_data.get("my_text"),
#             "my_email": received_data.get("my_email"),
#             "my_password": received_data.get("my_password"),
#             "my_date": received_data.get("my_date"),
#             "my_number": received_data.get("my_number"),
#             "my_checkbox": received_data.get("my_checkbox"),
#             "my_select": received_data.get("my_select"),
#             "my_textarea": received_data.get("my_textarea")
#         }, json_dumps_params={"ensure_ascii": False, "indent": 4})

def template_view(request):
    if request.method == "GET":
        return render(request, 'app/template_form.html')

    if request.method == "POST":
        received_data = request.POST  # Приняли данные в словарь
        form = TemplateForm(received_data)
        if form.is_valid():
            return JsonResponse(data=form.cleaned_data, json_dumps_params={"indent": 4, "ensure_ascii": False})
        return render(request, 'app/template_form.html', context={"form": form})
        # как пример получение данных по ключу `my_text`
        # my_text = received_data.get('my_text')

        # TODO Проведите здесь получение и обработку данных если это необходимо

        # TODO Верните HttpRequest или JsonResponse с данными


class TemplView(View):
    def get(self, request):
        return render(request, 'app/template_form.html')

    # TODO скопируйте код, что есть в template_view в теле условия request.method == "GET"
    def post(self, request):
        received_data = request.POST  # Приняли данные в словарь
        form = TemplateForm(received_data)
        print(form)
        if form.is_valid():
            return JsonResponse(data=form.cleaned_data, json_dumps_params={"indent": 4, "ensure_ascii": False})
        return render(request, 'app/template_form.html', context={"form": form})


class MyTemplView(TemplateView):
    template_name = 'app/template_form.html'

    def post(self, request, *args, **kwargs):
        received_data = request.POST  # Приняли данные в словарь
        form = TemplateForm(received_data)
        print(form)
        if form.is_valid():
            return JsonResponse(data=form.cleaned_data, json_dumps_params={"indent": 4, "ensure_ascii": False})
        context = self.get_context_data(**kwargs)
        context["form"] = form
        return self.render_to_response(context)


class MyFormView(FormView):
    template_name = 'app/template_form.html'
    form_class = TemplateForm
    success_url = '/'

    def form_valid(self, form):
        return JsonResponse(data=form.cleaned_data,
                            json_dumps_params={"indent": 4,
                                               "ensure_ascii": False})


# TODO скопируйте код, что есть в template_view в теле условия request.method == "POST"


# def login_view(request):
#     if request.method == "GET":
#         return render(request, 'app/login.html')
#
#     if request.method == "POST":
#         data = request.POST
#         user = authenticate(username=data["username"], password=data["password"])
#         if user:
#             login(request, user)
#             return redirect("app:user_profile")
#         return render(request, "app/login.html", context={"error": "Неверные данные"})
def login_view(request):
    if request.method == "GET":
        return render(request, 'app/login.html')

    if request.method == "POST":
        data = request.POST
        form = AuthenticationForm(request, data)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("app:user_profile")
        return render(request, "app/login.html", context={"form": form})


class MyLoginView(LoginView):
    template_name = 'app/login.html'
    form_class = AuthenticationForm
    redirect_authenticated_user = True  # Данный флаг не позволит авторизированному
    # пользователю зайти на страницу с авторизацией и сразу его перенаправит на
    # ссылку редиректа. По умолчанию redirect_authenticated_user = False




def logout_view(request):
    if request.method == "GET":
        logout(request)
        return redirect("/")


def register_view(request):
    if request.method == "GET":
        return render(request, 'app/register.html')

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Возвращает сохраненного пользователя из данных формы
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')  # Авторизируем пользователя
            return redirect("app:user_profile")

        return render(request, 'app/register.html', context={"form": form})


def index_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("app:user_profile")
        return render(request, 'app/index.html')


def user_detail_view(request):
    if request.method == "GET":
        return render(request, 'app/user_details.html')


def get_text_json(request):
    if request.method == "GET":
        return JsonResponse({"text": get_random_text()},
                            json_dumps_params={"ensure_ascii": False})
