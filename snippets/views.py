from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Snippet, Tag
from .serializers import SnippetSerializer, TagSerializer
from django.contrib.auth import authenticate
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.views import redirect_to_login
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class APIRootView(APIView):
    permission_classes = [AllowAny] 

    def get(self, request, format=None):
        return Response({
            "snippets": request.build_absolute_uri(reverse("snippet-list")),
            "tags": request.build_absolute_uri(reverse("tag-list")),
            "snippets-overview": request.build_absolute_uri(reverse("snippet-overview")),
            "swagger": request.build_absolute_uri(reverse("swagger-ui")),
        })


@method_decorator(csrf_exempt, name="dispatch")
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

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect_to_login(request.get_full_path(), login_url='/admin/login/')
        return super().dispatch(request, *args, **kwargs)

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
    
class SnippetOverviewAPIView(APIView):
    def get(self, request, *args, **kwargs):
        snippets = Snippet.objects.all()
        snippet_list = [
            {
                "id": snippet.id,
                "title": snippet.title,
                "detail_url": request.build_absolute_uri(reverse('snippet-detail', kwargs={'pk': snippet.id}))
            }
            for snippet in snippets
        ]
        
        return Response({
            "total_snippets": snippets.count(),
            "snippets": snippet_list
        })
