from django.urls import path, include
from .views import SubscriberViewSet, ContentViewSet
from rest_framework_nested import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Newsletters Suscription Service API",
      default_version='v1',
      description="Description of app",
      license=openapi.License(
         name="MIT License",
         url="",
      ),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register('contents', ContentViewSet, basename='content')




urlpatterns = [
    path("", include(router.urls)),
    path("subscribers", SubscriberViewSet.as_view({'post': 'create'})),
    path("subscribers/<str:email>/", SubscriberViewSet.as_view({'delete': 'destroy'})),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
