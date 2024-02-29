from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from audio.models import AudioModel


class AudioListAPIViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('audio-list')

    def test_audio_list_api_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class AudioAPIViewTestCase(TestCase):
    def setUp(self):
        self.audio_data = {
            'audio_id': '2kGMGxlrbOLhRzGQISekBZ',
            'title': 'Test Audio',
            'danceability': 0.7,
            'energy': 0.8,
            'key': 7,
            'loudness': -5.0,
            'mode': True,
            'acousticness': 0.3,
            'instrumentalness': 0.5,
            'liveness': 0.2,
            'valence': 0.6,
            'tempo': 120.0,
            'duration_ms': '300000',
            'time_signature': 4,
            'num_bars': 10,
            'num_sections': 5,
            'num_segments': 20,
            'audio_class': False,
            'rating': None
        }
        self.client = APIClient()
        self.audio = AudioModel.objects.create(**self.audio_data)
        self.url = reverse('audio-detail', args=[self.audio.title])
        self.valid_payload = {'danceability': 0.7}

    def test_get_audio_api_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_audio_api_view(self):
        response = self.client.patch(self.url, {"rating": 4}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['rating'], 4)

    def test_patch_invalid_audio_api_view(self):
        invalid_payload = {'rating': 6}
        response = self.client.patch(self.url, invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
