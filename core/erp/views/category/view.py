from random import random

from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView

from core.erp.forms import CategoryForm
from core.erp.models import Category


def category_list(request):
  data = {
    'title' : 'Category List',
    'categories' : Category.objects.all()

  }
  return render(request, 'category/list.html', data)

class CategoryListView(ListView):
  model =Category
  template_name = 'category/list.html'

  @method_decorator(csrf_exempt)
  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    data = {}
    try:
      data = Category.objects.get(pk=request.POST['id']).toJson()
    except Exception as e:
      data['error'] = str(e)
    return JsonResponse(data)

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

  def post(self, request, *args, **kwargs):
    data = {}
    try:
      action = request.POST['action']
      if action == 'add':
        form = self.get_form()
        if form.is_valid():
          form.save()
        else:
          data['error'] = form.errors
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

