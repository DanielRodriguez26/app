from django.contrib.auth import login, logout
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, RedirectView
import config.settings as setting

class LoginFormView(LoginView):
  template_name = 'login.html'

  def dispatch(self, request, *args, **kwargs):
    if request.user.is_authenticated:
      return redirect(setting.LOGIN_REDIRECT_URL)
    return super().dispatch(request, *args, **kwargs)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'LOG IN'
    return context

class LoginFormView2(FormView):
  form_class = AuthenticationForm
  template_name = 'login.html'
  success_url = reverse_lazy('erp:category_list')

  def dispatch(self, request, *args, **kwargs):
    if request.user.is_authenticated:
      return redirect(setting.LOGIN_REDIRECT_URL)
    return super().dispatch(request, *args, **kwargs)

  def form_valid(self, form):
    login(self.request, form.get_user() )
    return  HttpResponseRedirect(self.success_url)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'LOG IN'
    return context

class LogoutRedirectView(RedirectView):
  pattern_name = 'login'

  def dispatch(self, request, *args, **kwargs):
    logout(request)
    return super().dispatch(request, *args, **kwargs)