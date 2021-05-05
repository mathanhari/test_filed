from django.contrib import admin
from .models import *

admin.site.register(AudiobookModel)
admin.site.register(SongModel)
admin.site.register(PodcastModel)