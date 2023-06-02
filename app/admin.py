from django.contrib import admin
from django.contrib.admin import site
# Register your models here.

from app.models import Cliente
site.register(Cliente)