# from django.db.models import QuerySet

from config.wsgi import *
from core.erp.models import Category

#listar
# query = Type.objects.all()
# print(list)

# t = Category()
# t.name = 'Dairy products'
# t.save()

# Editar
# t = Type.objects.get(id=2)
# t.name = 'Accionista'
# t.save()


#Eliminar
# t = Category.objects.get(pk=1)
# t.delete()



print(Category.objects.all())

for i in Category.objects.filter():
  print(i)

