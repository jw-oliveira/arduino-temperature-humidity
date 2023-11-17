from django.urls import path
from . import views
from .views import RecordsCreateView

app_name = 'arduino'

urlpatterns = [
    path('/index', views.index, name='index'),
    path('/input_data', RecordsCreateView.as_view(), name='input_data')
]