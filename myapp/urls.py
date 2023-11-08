from django.urls import path, include
from . import views
urlpatterns = [
    path('<int:start>/<int:end>', views.index, name='index'),
    path('', views.index, name='index'),
]
