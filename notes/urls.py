from django.urls import path

from notes import views

urlpatterns = [
    path('notes', views.list),
    path('notes/<int:pk>', views.detail)
]