from django.urls import path
from .views import PostView, PostDetailView

urlpatterns = [
    path('post', PostView.as_view()),
    path('post/<int:id>', PostDetailView.as_view()),
]
