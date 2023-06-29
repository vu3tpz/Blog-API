from django.urls import path

from .views import PostDetailView, PostView

urlpatterns = [
    path("post", PostView.as_view()),
    path("post/<int:id>", PostDetailView.as_view()),
]
