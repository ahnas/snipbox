from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Snippet, Tag
from .serializers import SnippetSerializer, TagSerializer
from django.contrib.auth import authenticate
from django.shortcuts import render



class CustomLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email
                }
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
def login_page(request):
    return render(request, "login.html")

def home_page(request):
    return render(request, "home.html")

class SnippetListCreateView(generics.ListCreateAPIView):
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Snippet.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SnippetDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Snippet.objects.filter(user=self.request.user)

class TagListView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def post(self, request, *args, **kwargs):
        title = request.data.get("title")
        if not title:
            return Response({"error": "Title is required"}, status=status.HTTP_400_BAD_REQUEST)

        tag, created = Tag.objects.get_or_create(title=title)
        return Response(TagSerializer(tag).data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)
    

class TagDetailView(generics.ListAPIView):
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Snippet.objects.filter(tags__id=self.kwargs['pk'])
