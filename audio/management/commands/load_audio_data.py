
import json
from django.core.management.base import BaseCommand, CommandError
from audio.models import AudioModel


class Command(BaseCommand):
    help = "Load given json file into audio model"

    def add_arguments(self, parser):
        parser.add_argument("json_file", type=str)

    def handle(self, *args, **options):
        json_file = options['json_file']
        formatted_data: list[dict] = []
        with open(json_file, 'r') as f:
            data = json.load(f)

            if not data or not data.get('id'):
                return

            length = len(data['id'])

            data['audio_id'], data['audio_class'] = data.pop(
                'id'), data.pop('class')
            for index in range(length):
                str_index = str(index)
                value = {key: data[key][str_index] for key in data.keys()}
                formatted_data.append(value)
        
        AudioModel.objects.bulk_create((AudioModel(**value) for value in formatted_data))

