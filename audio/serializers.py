from rest_framework import serializers 
from audio.models import AudioModel


class AudioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AudioModel
        read_only_fields = ('audio_id', 'title', 'danceability',
                            'energy', 'key', 'loudness', 'mode',
                            'acousticness', 'instrumentalness',
                            'liveness', 'valence', 'tempo',
                            'duration_ms', 'time_signature',
                            'num_bars', 'num_sections', 'num_segments',
                            'audio_class')
        fields = ('audio_id', 'title', 'danceability',
                            'energy', 'key', 'loudness', 'mode',
                            'acousticness', 'instrumentalness',
                            'liveness', 'valence', 'tempo',
                            'duration_ms', 'time_signature',
                            'num_bars', 'num_sections', 'num_segments',
                            'audio_class', 'rating')