# news_project/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from admin_app.views import NewsAdminViewSet
from user_app.views import NewsUserViewSet

router = DefaultRouter()
router.register(r'admin/news', NewsAdminViewSet, basename='admin-news')
router.register(r'user/news', NewsUserViewSet, basename='user-news')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
