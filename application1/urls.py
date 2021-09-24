
from django.urls import path
from .import views

urlpatterns = [
    path('test',views.testfun,name='test'),
    path('index',views.indexfun,name='index'),


]
