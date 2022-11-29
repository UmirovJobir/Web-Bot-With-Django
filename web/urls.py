from django.urls import path
from . import views

urlpatterns = [
    path('catalogue/', views.catalogueView, name='catalogue')
]
