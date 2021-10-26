from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """ Example of API View """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return list of APIView features"""
        an_apiview = [
            'Using HTTP mehtods like functions (get, post, patch, put, delete)',
            'Is similar to a traditional view of Django',
            'We have more control about our app logic',
            'Is mapped to the URLs'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a message with my name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )    