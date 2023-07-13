from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from location.models import Province, City 

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class CityList(APIView):
    permission_classes = [IsAuthenticated,]
    
    def post(self, request, format=None):
        id = request.data['id']
        location = {}
        if id:
            locations = City.objects.filter(provId=id)
            location = {p.cityDesc:p.id for p in locations}
        return JsonResponse(data=location, safe=False)