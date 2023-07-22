from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from django.http import Http404


class CommonCreateListAPIView(APIView):
    """
    `CommonCreateListAPIView` is common view used to `create` and `list`. Method used in the
    view is `GET` and `POST`. You need to provide `serializer_class` and `model_class`,
    by providing this you can create and list the objects for your model and serializer.
    """

    serializer_class = None
    model_class = None

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            data = serializer.save(created_by=self.request.user)

            # User to handle `ManyToMany` Field in Role Model
            if self.model_class == "Role":
                """
                This `if condition` check the model is `Role` if it is, then it execute this statements,
                to handle `ManyToMany` (permission) field.
                """

                # Get the permissions data from the validated serializer data
                permissions = self.request.data.get("permission", [])

                # Clear the existing permissions and set the new permissions
                data.permission.clear()
                data.permission.add(*permissions)

            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(data={"errors": serializer.errors}, status=HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        object = self.model_class.objects.all()
        serializer = self.serializer_class(object, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class CommonDetailAPIView(APIView):
    serializer_class = None
    model_class = None

    def get_object(self, id):
        try:
            return self.model_class.objects.get(id=id)
        except self.model_class.DoesNotExist:
            raise Http404

    def get(self, request, id):
        instance = self.get_object(id)
        serializer = self.serializer_class(instance)
        return Response(serializer.data, status=HTTP_200_OK)

    def put(self, request, id):
        instance = self.get_object(id)
        serializer = self.serializer_class(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        instance = self.get_object(id)
        instance.delete()
        return Response(data={"detail": "Data Delete Successfully"}, status=HTTP_200_OK)
