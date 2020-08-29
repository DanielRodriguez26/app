from random import random

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView

from core.erp.forms import CategoryForm
from core.erp.models import Category


class CategoryListView(ListView):
  model =Category
  template_name = 'category/list.html'

  @method_decorator(csrf_exempt)
  @method_decorator(login_required)
  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    data = {}
    try:
      action = request.POST['action']
      if action == 'searchdata':
        data = []
        for i in Category.objects.all():
          data.append(i.toJson())
      else:
        data['error'] = 'An error has occurred'
    except Exception as e:
      data['error'] = str(e)
    return JsonResponse(data, safe=False)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Category List'
    context['create_url'] = reverse_lazy('erp:category_create')
    context['list_url'] = reverse_lazy('erp:category_list')
    context['entity'] = 'Category'
    return context

class CategoryCreateView(CreateView):
  model = Category
  form_class = CategoryForm
  template_name = 'category/create.html'
  success_url = reverse_lazy('erp:category_list')

  @method_decorator(login_required)
  def dispatch(self, request, *args, **kwargs):
    self.object = self.get_object()
    return super().dispatch(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    data = {}
    try:
      action = request.POST['action']
      if action == 'add':
        form = self.get_form()
        data = form.save()
      else:
        data['error'] = 'You have not entered any option'
    except Exception as e:
      data['error'] = str(e)
    return JsonResponse(data)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Category Create'
    context['entity'] = 'Category'
    context['action'] = 'add'
    context['list_url'] = reverse_lazy('erp:category_list')
    return context

class CategoryUpdateView(UpdateView):
  model = Category
  form_class = CategoryForm
  template_name = 'category/create.html'
  success_url = reverse_lazy('erp:category_list')

  @method_decorator(login_required)
  def dispatch(self, request, *args, **kwargs):
    self.object = self.get_object()
    return super().dispatch(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    data = {}
    try:
      action = request.POST['action']
      if action == 'add':
        form = self.get_form()
        data = form.save()
      else:
        data['error'] = 'You have not entered any option'
    except Exception as e:
      data['error'] = str(e)
    return JsonResponse(data)

  def  get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Category Edit'
    context['entity'] = 'Category'
    context['action'] = 'edit'
    context['list_url'] = reverse_lazy('erp:category_list')
    return context

class CategoryDeleteView(DeleteView):
  model = Category
  form_class = CategoryForm
  template_name = 'category/delete.html'
  success_url = reverse_lazy('erp:category_list')

  @method_decorator(login_required)
  def dispatch(self, request, *args, **kwargs):
    self.object = self.get_object()
    return super().dispatch(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    data = {}
    try:
      self.object.delete()
    except Exception as e:
      data['error'] = str(e)
    return JsonResponse(data)

  def  get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Category Delete'
    context['entity'] = 'Category'
    context['list_url'] = reverse_lazy('erp:category_list')
    return context

