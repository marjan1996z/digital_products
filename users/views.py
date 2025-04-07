import uuid

import random

from asgiref.timeout import timeout
from django.core.cache import cache

from django.shortcuts import render
from django.template.context_processors import request
from django.utils.text import phone2numeric
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User, Device

class RegisterView(APIView):

    def post(self, request):
        phone_number = request.data.get('phone_number')
        if not phone_number:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(phone_number=phone_number)
            return Response({'detail': 'User already registered!'},
                            status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            user = User.objects.create_user(phone_number=phone_number)


        device = Device.objects.create(user=user)

        code = random.randint(10000, 99999)

        cache.set(str(phone_number), code, timeout=120)

        return Response({'code': code})

class GetTokenView(APIView):

    def post(self, request):
        phone_number = request.data.get('phone_number')
        code = request.data.get('code')

        cached_code = cache.get(str(phone_number))

        if cached_code is None:
            return Response({'detail': 'Code has expired or does not exist.'},
                            status=status.HTTP_400_BAD_REQUEST)

        if code != cached_code:
            return Response({'detail': 'Invalid code.'},
                            status=status.HTTP_403_FORBIDDEN)

        token = str(uuid.uuid4())

        return Response({'token': token})