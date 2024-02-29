from django.urls import path
from audio.views import AudioListAPIView,AudioAPIView


urlpatterns = [
    path('', AudioListAPIView.as_view(), name='audio-list'),
    path('<str:title>/', AudioAPIView.as_view(), name='audio-detail')
]
