from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    # (Название, model.view, параметри)
    path('', views.index, name='index'),
    path('<int:course_id>', views.course, name='course'),
]
