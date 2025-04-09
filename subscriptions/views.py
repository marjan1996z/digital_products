from datetime import timezone

from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.schemas.coreapi import is_enabled
from rest_framework.views import APIView

from subscriptions.models import Package, Subscription
from subscriptions.serializers import PackageSerializer, SubscriptionSerializer


class PackageView(APIView):
    def get(self, request):
        packges = Package.objects.filter(is_enabled=True)
        serializer = PackageSerializer(packges, many=True)
        return Response(serializer.data)

class SubscriptionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        subscriptions = Subscription.objects.filter(
            user=request.user,
            expire_time__gt=timezone.now()
        )
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data)