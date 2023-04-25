from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View

from .forms import LoginForm, SignupForm


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('posts:index')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')
    http_method_names = ['post', ]


class SignupView(View):
    template_name = 'users/signup.html'
    form = SignupForm

    def get_context_data(self):
        context = {
            'form': self.form
        }

        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST, request.FILES)
        context = self.get_context_data()
        context['form'] = form

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('posts:index'))
        else:
            return render(request, self.template_name, context)



