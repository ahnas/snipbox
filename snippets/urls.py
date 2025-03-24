from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import SnippetListCreateView, SnippetDetailView, TagListView, TagDetailView, CustomLoginView, SnippetOverviewAPIView, APIRootView

urlpatterns = [
    path('', APIRootView.as_view(), name='api-root'),
    path('snippets/', SnippetListCreateView.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', SnippetDetailView.as_view(), name='snippet-detail'),
    path('tags/', TagListView.as_view(), name='tag-list'),
    path('tags/<int:pk>/', TagDetailView.as_view(), name='tag-detail'),

    path('auth/login/', CustomLoginView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('snippets/overview/', SnippetOverviewAPIView.as_view(), name='snippet-overview'),
]
