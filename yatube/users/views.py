# Импортируем CreateView, чтобы создать ему наследника
from django.views.generic import CreateView

# Функция reverse_lazy позволяет получить URL по параметрам функции path()
# Берём, тоже пригодится
from django.urls import reverse_lazy

# Импортируем класс формы, чтобы сослаться на неё во view-классе
from .forms import CreationForm
# from django.contrib.auth.forms import PasswordResetForm

class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'

# class PasswordResetView(CreateView):
#     form_class = PasswordResetForm
#     success_url = reverse_lazy('posts:index')
#     template_name = 'users/password_reset_form.html'
