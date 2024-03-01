from django.shortcuts import get_object_or_404

from audio.models import AudioModel
from audio.serializers import AudioSerializer

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status


class AudioListAPIView(ListAPIView):
    serializer_class = AudioSerializer
    queryset = AudioModel.objects.all().order_by('-created_at')
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10


class AudioAPIView(APIView):
    serializer_class = AudioSerializer
    queryset = AudioModel.objects.all()
    lookup_field = 'title'

    def get(self, request, title):
        audio = get_object_or_404(AudioModel, title=title)
        audio_serializer = self.serializer_class(audio)
        return Response(audio_serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, title):
        audio = get_object_or_404(AudioModel, title=title)
        audio_serializer = self.serializer_class(
            audio, data=request.data, partial=True)

        if audio_serializer.is_valid():
            audio_serializer.save()
            return Response(audio_serializer.data, status=status.HTTP_200_OK)
        return Response(audio_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
