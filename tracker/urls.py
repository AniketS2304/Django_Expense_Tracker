from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:id>/', views.delete_transaction, name='delete_transaction'),
    path('delete_all_transactions/', views.delete_all_transactions, name='delete_all_transactions')
]