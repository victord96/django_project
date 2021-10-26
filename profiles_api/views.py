from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """ Example of API View """

    def get(self, request, format=None):
        """Return list of APIView features"""
        an_apiview = [
            'Using HTTP mehtods like functions (get, post, patch, put, delete)',
            'Is similar to a traditional view of Django',
            'We have more control about our app logic',
            'Is mapped to the URLs'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})