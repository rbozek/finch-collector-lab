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

  path('monkeys/<int:monkey_id>/add-brushing/', views.add_brushing, name='add-brushing'),

  # will this create plural/spelling issue??
  path('accessories/create/', views.AccessoryCreate.as_view(), name='accessory-create'),
  path('accessories/<int:pk>/', views.AccessoryDetail.as_view(), name='accessory-detail'),
  path('accessories/', views.AccessoryList.as_view(), name='accessory-index'),

  path('accessories/<int:pk>/update/', views.AccessoryUpdate.as_view(), name='accessory-update'),
  path('accessories/<int:pk>/delete/', views.AccessoryDelete.as_view(), name='accessory-delete'),
]