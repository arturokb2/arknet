from django.http.response import JsonResponse,HttpResponse
from rest_framework.response import Response
from  rest_framework import generics, serializers,status
from rest_framework.views import APIView
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import (SearchHistorySerializers,
                          HistorySerializers,
                          PatientUpdateSerializers,
                          SluchayUpdateSerializers)
from hospital.models import Sluchay,Patient

# class Form7ListAPIView(generics.ListAPIView):
#     serializer_class = Form7Serializers
#     def get(self, request, *args, **kwargs):
#         queryset = self.get_queryset(self,*args, **kwargs)
#         serializer = Form7Serializers(queryset,many=True)
#         return Response(serializer.data)
    
#     def get_queryset(self,*args, **kwargs):
#         return Form_7.objects.all()

class SearchHistoryListAPIView(generics.ListAPIView):
    serializer_class = SearchHistorySerializers

    def get(self,request, *args, **kwargs):
        queryset = self.get_queryset(self,*args, **kwargs)
        serializer = SearchHistorySerializers(queryset,many=True)
        return Response(serializer.data)
    #
    def get_queryset(self,*args, **kwargs):
        nib = self.request.GET.get('nib', None)
        if nib is not None:
            return Sluchay.objects.filter(nib__icontains=nib)[:10]
        else:
            return Sluchay.objects.all()[:10]

class History(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HistorySerializers
    queryset = Sluchay.objects.all()
    # def get_object(self, pk):
    #     try:
    #         return Sluchay.objects.get(pk=pk)
    #     except Sluchay.DoesNotExist:
    #         raise Http404
    #
    # def get(self, request, pk):
    #     snippet = self.get_object(pk)
    #     serializer = HistorySerializers(snippet)
    #     return Response(serializer.data)
    #
    # def put(self, request, pk):
    #     snippet = self.get_object(pk)
    #     serializer = HistorySerializers(snippet, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class PatientUpdateAPIView(generics.UpdateAPIView):
#     serializer_class = PatientUpdateSerializers
#     queryset = Patient.objects.all()
@csrf_exempt
def PatientUpdate(request,pk):
    try:
        patient = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return HttpResponse(status=404)
        
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PatientUpdateSerializers(patient,data=data)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse({'rez':'PatientUpdate'})

@csrf_exempt
def SluchayUpdate(request,pk):
    try:
        sluchay = Sluchay.objects.get(pk=pk)
    except Sluchay.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SluchayUpdateSerializers(sluchay,data=data)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse({'rez':'SluchayUpdate'})