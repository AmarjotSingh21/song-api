# song-api

Install dependencies
```bash
pip install -r requirements.txt
```

Make migrations
```bash
python manage.py makemigrations
```

Migrate migrations
```bash
python manage.py migrate
```

Load audio data to database
```bash
python manage.py load_audio_data playlist.json
```


Run server
```bash
python manage.py runserver
```


Test
```bash
python manage.py test
```


Clean database
```bash
python manage.py flush
```