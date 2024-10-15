from django.urls import path

from .views import DataView

urlpatterns = [
    path('dates/', DataView.as_view()),
]