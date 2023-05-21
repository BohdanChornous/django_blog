from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts", views.AllPostsView.as_view(), name="post-page"),
    path("posts/<slug:slug>", views.PostDetailView.as_view(), name="post-details-page"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later"),
]
