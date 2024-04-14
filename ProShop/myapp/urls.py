from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:my_id>/', views.indexItem, name='detail'),
]
