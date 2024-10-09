from django.urls import path
from . import views

urlpatterns = [
    path('database_view/', views.database_view, name='database_view'),  # 예시 URL
]
