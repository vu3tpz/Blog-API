from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK


class CommonCreateListAPIView(APIView):
    """
    `CommonCreateListAPIView` is common view used to `create` and `list`. Method used in the
    view is `GET` and `POST`. You need to provide `serializer_class` and `model_class`,
    by providing this you can create and list the objects for your model and serializer.
    """

    serializer_class = None
    model_class = None

    def post(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            data = serializer.save()

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

            return Response(data=serializer.data, status=HTTP_201_CREATED)
        return Response(data={"errors": serializer.errors}, status=HTTP_400_BAD_REQUEST)

    def get(self, *args, **kwargs):
        object = self.model_class.objects.all()
        serializer = self.serializer_class(object, many=True)
        return Response(data=serializer.data, status=HTTP_200_OK)
