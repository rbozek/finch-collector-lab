from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('monkeys/', views.monkey_index, name='monkey-index'),
  path('monkeys/<int:monkey_id>/', views.monkey_detail, name='monkey-detail'),
]