from operator import index

from django.contrib import admin
from django.urls import path
from employeApp import views
from employeApp.views import delete

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('addrec/', views.addrec, name='addrec'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('uprec/<int:id>/', views.uprec, name='uprec'),
    path('admin/', admin.site.urls),
]
