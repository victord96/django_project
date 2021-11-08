from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers, models, permissions


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

    def put(self, request, pk=None):
        """Update an object"""
        return Response({'method': 'PUT'})

    def patch(self, response, pk=None):
        """Allow parcial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, response, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})    

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet""" 

    serializer_class = serializers.HelloSerializer
         
    def list(self, request):
        """Return Hello World message""" 

        a_viewset = [
            "Use actions (list, create, retrieve, update, partial_update",
            "Automatically map out the URL's using routers",
            "Provides more functionality with less code",
        ]

        return Response({'message': 'Hola!', 'a_viewset': a_viewset})

    def create(self, request):
        """ Create new message Hello World"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )   

    def retrieve(self, request, pk=None):
        """Return an object and the ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Update and object"""
        return Response({'http_method': 'PUT'})   

    def partial_update(self, rquest, pk=None):
        """Update a partial object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Destroy an object"""
        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """ Create and update profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)