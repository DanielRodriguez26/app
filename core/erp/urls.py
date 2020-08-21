from django.urls import path

from core.erp.views import myfirstview

urlpatterns = [

    path('prueba/', myfirstview)
]
