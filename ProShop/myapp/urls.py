from django.urls import path
from myapp import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:my_id>/', views.indexItem, name='detail'),
    path("add/", views.addItem, name='addItem'),
    path("update/<int:my_id>/", views.update, name='update'),
    path("delete/<int:my_id>/", views.delete, name='delete'),
]
