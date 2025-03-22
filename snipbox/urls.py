from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from snippets.views import login_page, home_page


schema_view = get_schema_view(
    openapi.Info(
        title="SnipBox API",
        default_version="v1",
        description="API documentation for SnipBox Backend",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('snippets.urls')),
    path('',login_page, name="login_page"),
    path('home/', home_page, name="home_page"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger-ui"),
]
