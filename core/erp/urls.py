from django.urls import path

from core.erp.views.category.view import *
from core.erp.views.dashboard.dashboard import DashboardView

app_name = 'erp'
urlpatterns = [

    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),

    # Home
    path('dashboard/', DashboardView.as_view(), name='dashboard'),


]
