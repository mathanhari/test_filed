from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

class AudioView(APIView):

    def get(self, request):
        songobj = SongModel.objects.all()
        podcastobj = PodcastModel.objects.all()
        audiobookobj = AudiobookModel.objects.all()
        songserial = SongSerializer(songobj, many=True)
        podserial = PodcastSerializer(podcastobj, many=True)
        audiobookserial = AudiobookSerializer(audiobookobj, many=True)
        return Response({'song': songserial.data, 'podcast': podserial.data, 'audiobook': audiobookserial.data})

    def post(self, request):
        songserial = SongSerializer(data=request.data)
        podserial = PodcastSerializer(data=request.data)
        audiobookserial = AudiobookSerializer(data=request.data)
        if songserial.is_valid() and podserial.is_valid() and audiobookserial.is_valid():
            songserial.save()
            podserial.save()
            audiobookserial.save()
            return Response({'song': songserial.data, 'podcast': podserial.data, 'audiobook': audiobookserial.data})
        return Response(songserial.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        songobj = SongModel.objects.get(id=pk).delete()
        podcastobj = PodcastModel.objects.get(id=pk).delete()
        audiobookobj = AudiobookModel.objects.get(id=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
