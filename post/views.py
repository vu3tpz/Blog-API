from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .serializer import PostSerializer


# Create your views here.
class PostView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = {
            "title": request.data.get("title"),
            "description": request.data.get("description"),
            "created_by": self.request.user.id,
        }
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get_object(self, request, id):
        try:
            return Post.objects.get(id=id)
        except Post.DoesNotExist:
            return None

    def get(self, request, id):
        post = self.get_object(request, id=id)
        if not post:
            return Response(
                {"error": "There is no post with this ID."},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        post = self.get_object(request, id)
        if not post:
            return Response(
                {"error": "There is no post with this ID."},
                status=status.HTTP_404_NOT_FOUND,
            )
        data = request.data
        serializer = PostSerializer(instance=post, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
