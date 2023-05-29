from django.urls import path
from .views import PostView, PostDetailView

urlpatterns = [
    path('api', PostView.as_view()),
    path('api/<int:id>', PostDetailView.as_view()),
]
