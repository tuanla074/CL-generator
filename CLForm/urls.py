from django.urls import path
from . import views


app_name = 'CLgen'

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:rec_id>/', views.generated, name="generated"),
]