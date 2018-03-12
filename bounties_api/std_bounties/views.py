from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Count
from django.http import JsonResponse, Http404
from rest_framework.views import APIView
from std_bounties.constants import STAGE_CHOICES
from std_bounties.models import Bounty, Fulfillment, RankedCategory
from std_bounties.serializers import BountySerializer, FulfillmentSerializer, RankedCategorySerializer
from std_bounties.filters import BountiesFilter, FulfillmentsFilter
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework_filters.backends import DjangoFilterBackend


class BountyViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = BountySerializer
    queryset = Bounty.objects.all()
    filter_class = BountiesFilter
    filter_backends = (OrderingFilter, SearchFilter, DjangoFilterBackend,)
    ordering_fields = ('fulfillmentAmount', 'deadline', 'bounty_created', 'usd_price')
    search_fields = ('title', 'description', 'categories__normalized_name')


class FulfillmentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = FulfillmentSerializer
    queryset = Fulfillment.objects.all()
    filter_class = FulfillmentsFilter
    filter_backends = (DjangoFilterBackend,)


class CategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = RankedCategorySerializer
    queryset = RankedCategory.objects.all()
    filter_backends = (OrderingFilter, SearchFilter, DjangoFilterBackend,)
    ordering_fields = ('total_count',)
    ordering = ('-total_count',)
    search_fields = ('normalized_name',)

class BountyStats(APIView):
    def get(self, request, address=''):
        bounty_stats = {}
        user_bounties = Bounty.objects.filter(issuer=address)
        for stage in STAGE_CHOICES:
            bounty_stats[stage[1]] = user_bounties.filter(bountyStage=stage[0]).count()
        return JsonResponse(bounty_stats)

