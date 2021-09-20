from django.urls import path
from . import views

urlpatterns = [
    # path('print_number/',views.print_number,name='print_number'),
    path('base/',views.base,name='base'),
]