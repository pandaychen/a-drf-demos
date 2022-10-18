from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from swaggerEx import views

router = routers.DefaultRouter()
router.register('api_info', views.APIInfoViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title="测试工程API",
        default_version='v1.0',
        description="测试工程接口文档",
        terms_of_service="",
        contact=openapi.Contact(email="xxxx@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),

    # 配置django-rest-framwork API路由
    path('api/', include('swaggerEx.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),


    # 配置drf-yasg路由
    url('^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(
        cache_timeout=0), name='schema-json'),
    path('swagger', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),

]
