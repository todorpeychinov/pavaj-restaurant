from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from menu.models import MenuType
from rest_api.serializers import MenuTypeSerializer


# Create your views here.


class MenuAPIView(APIView):
    def get(self, request, *args, **kwargs):
        menu_types = MenuType.objects.prefetch_related(
            'categories__items__allergens'
        ).all()

        serializer = MenuTypeSerializer(menu_types, many=True)
        return Response(serializer.data)
