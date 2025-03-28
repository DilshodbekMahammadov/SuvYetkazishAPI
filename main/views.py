from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *

class MyPageNumberPegination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 100

class SuvAPIView(APIView):
    def get(self, request):
        suv = Suv.objects.all()
        serializer = SuvSerializer(suv, many=True)
        return Response(serializer.data)
    @swagger_auto_schema(request_body=SuvSerializer)
    def post(self, request):
        serializer = SuvSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class SuvRetriveUpdateDeleteAPIView(APIView):
    def get(self, pk):
        suv = Suv.objects.get(pk=pk)
        serializer = SuvSerializer(suv)
        return Response(serializer.data)

    def put(self, request, pk):
        suv = Suv.objects.get(pk=pk)
        serializer = SuvSerializer(instance=suv, data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {
                'success': True,
                'massage': 'Suv ma\'lumoti muvaffaqqiyatli o\'zgartirildi.',
                'data' : serializer.data
            }
            return Response(res, status=200)
        response = {
            'success': False,
            'massage': 'Suv ma\'lumoti muvaffaqqiyatli o\'zgartirilmadi.',
            'data' : serializer.errors
        }
        return Response(response, status=400)

    def delete(self, pk):
        suv = Suv.objects.get(pk=pk)
        suv.delete()
        return Response(status=204)

class MijozAPIView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='search',
                in_=openapi.IN_QUERY,
                description='Ism va tel orqali qidiruv',
                type=openapi.TYPE_STRING,
            )
        ]
    )
    def get(self):
        mijoz = Mijoz.objects.all()
        search = self.request.GET.get('search')
        if search is not None:
            mijoz = mijoz.filter(mijoz__icontains=search)
        else:
            mijoz = mijoz.all()
        serializer = MijozSerializer(mijoz, many=True)
        return Response(serializer.data)
    @swagger_auto_schema(request_body=MijozSerializer)
    def post(self, request):
        serializer = MijozSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class MijozRetriveUpdateDeleteAPIView(APIView):
    def get(self, request, pk):
        mijoz = Mijoz.objects.get(pk=pk)
        serializer = MijozSerializer(mijoz)
        return Response(serializer.data)

    def put(self, request, pk):
        mijoz = Mijoz.objects.get(pk=pk)
        serializer = MijozSerializer(instance=mijoz, data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {
                'success': True,
                'massage': 'Mijoz ma\'lumoti muvaffaqqiyatli o\'zgartirildi.',
                'data' : serializer.data
            }
            return Response(res, status=200)
        response = {
            'success': False,
            'massage': 'Mijoz ma\'lumoti muvaffaqqiyatli o\'zgartirilmadi.',
            'data' : serializer.errors
        }
        return Response(response, status=400)

    def delete(self, pk):
        mijoz = Mijoz.objects.get(pk=pk)
        mijoz.delete()
        return Response(status=204)

class BuyurtmaListCreateAPIView(ListCreateAPIView):
    serializer_class = BuyurtmaSerializer
    queryset = Buyurtma.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = MyPageNumberPegination
    filter_backends = [ OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['sana']
    filterset_fields = ['suv', 'mijoz']



class AdministratorListAPIView(ListAPIView):
    serializer_class = AdministratorSerializer
    queryset = Administrator.objects.all()
    permission_classes = [IsAuthenticated]

class AdministratorRetriveAPIView(RetrieveAPIView):
    serializer_class = AdministratorSerializer
    queryset = Administrator.objects.all()
    permission_classes = [IsAuthenticated]

class HaydovchiListAPIView(ListAPIView):
    serializer_class = HaydovchiSerializer
    queryset = Haydovchi.objects.all()
    permission_classes = [IsAuthenticated]

class HaydovchiRetriveAPIView(RetrieveAPIView):
    serializer_class = HaydovchiSerializer
    queryset = Haydovchi.objects.all()
    permission_classes = [IsAuthenticated]