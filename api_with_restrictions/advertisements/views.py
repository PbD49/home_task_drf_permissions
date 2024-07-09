from rest_framework.authentication import TokenAuthentication
from .permissions import IsOwnerOrReadonly
from rest_framework.viewsets import ModelViewSet

from .filter import AdvertisementFilter
from .models import Advertisement
from .serializers import AdvertisementSerializer
from django_filters import rest_framework as filters


class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = AdvertisementFilter
    permission_classes = [IsOwnerOrReadonly, ]
