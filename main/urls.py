from django.contrib import admin
from django.urls import path
from .views import home,detail,delete,update,create


urlpatterns = [
    path("",home,name='home'),
    path("detail/<int:pk>/",detail,name="detail"),
    path("delete/<int:pk>/",delete,name="delete"),
    path("update/<int:pk>/",update,name="update"),
    path("create/",create,name="create")

]


