from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('monkeys/', views.monkey_index, name='monkey-index'),
  path('monkeys/<int:monkey_id>/', views.monkey_detail, name='monkey-detail'),
  # using CBV's below:
  path('monkeys/create/', views.MonkeyCreate.as_view(), name='monkey-create'),
  path('monkeys/<int:pk>/update/', views.MonkeyUpdate.as_view(), name='monkey-update'),
  path('monkeys/<int:pk>/delete/', views.MonkeyDelete.as_view(), name='monkey-delete'),
]