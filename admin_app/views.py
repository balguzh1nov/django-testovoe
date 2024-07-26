# admin_app/views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from news.models import News
from news.serializers import NewsSerializer

class NewsAdminViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAdminUser]
