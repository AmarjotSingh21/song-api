from django.test import TestCase
from audio.models import AudioModel

class AudioModelTestCase(TestCase):
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

    def test_audio_model_creation(self):
        audio = AudioModel.objects.create(**self.audio_data)
        self.assertEqual(audio.audio_id, '2kGMGxlrbOLhRzGQISekBZ')
        self.assertEqual(audio.title, 'Test Audio')
