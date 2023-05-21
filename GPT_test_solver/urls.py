from django.urls import path
from . import views

urlpatterns = [
    path("test_solver", views.TestSolvView.as_view(), name="test_solver")
]
