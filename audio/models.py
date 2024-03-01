from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class AudioModel(models.Model):
    audio_id = models.CharField(
        primary_key=True, max_length=22, db_column="id", verbose_name="id")
    title = models.CharField(max_length=300, unique=True)
    danceability = models.FloatField(
        validators=[MaxValueValidator(1), MinValueValidator(0)])
    energy = models.FloatField(
        validators=[MaxValueValidator(1), MinValueValidator(0)])
    key = models.PositiveSmallIntegerField()
    loudness = models.FloatField(validators=[MaxValueValidator(0)])
    mode = models.PositiveSmallIntegerField()
    acousticness = models.FloatField(
        validators=[MaxValueValidator(1), MinValueValidator(0)])
    instrumentalness = models.FloatField(
        validators=[MaxValueValidator(1), MinValueValidator(0)])
    liveness = models.FloatField(
        validators=[MaxValueValidator(1), MinValueValidator(0)])
    valence = models.FloatField(
        validators=[MaxValueValidator(1), MinValueValidator(0)])
    tempo = models.FloatField()
    duration_ms = models.CharField(max_length=10)
    time_signature = models.PositiveSmallIntegerField()
    num_bars = models.PositiveSmallIntegerField()
    num_sections = models.PositiveSmallIntegerField()
    num_segments = models.PositiveSmallIntegerField()
    audio_class = models.PositiveSmallIntegerField(db_column="class", verbose_name="class")
    rating = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)], null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "audio"

    def __str__(self) -> str:
        return self.audio_id
