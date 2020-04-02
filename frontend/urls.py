from django.urls import path, include
from . import views
from . import forms
from .views import Questions

urlpatterns = [
    path('', views.MainView.as_view()),
    path('recrut/', views.form),
    path('recrut/add/', views.recrut_add),
    path('test/', Questions.as_view())

]
