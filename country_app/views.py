from rest_framework import generics
from .models import Country
from .serializers import CountrySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .filters import CountryFilter
from django.core.cache import cache
import logging
from rest_framework.response import Response

logger = logging.getLogger('country_app')

class CountryList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_class = CountryFilter
    search_fields = ['name', 'id']
    def list(self, request, *args, **kwargs):
        query_params = request.query_params
        cache_key = f'country_list:{query_params}'
        data = cache.get(cache_key)
        if data:
            logger.info('data retrieved from cache')
        else:
            logger.info('data retrieved from db')
            filtered_queryset = self.filter_queryset(self.get_queryset())
            data = CountrySerializer(filtered_queryset, many=True).data
            cache_time = 60 * 5
            cache.set(cache_key, data, cache_time)
        return Response(data)


class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer