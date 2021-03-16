from re import L
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Note
from .serializers import NoteSerializer

# Create your views here.


class NoteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get(self, request):
        data = [{"title": data.title, "description": data.description}
                for data in Note.objects.all()]
        print("request data get :", data)
        return Response(data)

    def post(self, request):

        serializer = NoteSerializer(data=request.data)
        print("request data post :", request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
