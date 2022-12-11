from django.db import models

class ChatConsumer(models.Model):
    room_name = models.CharField(max_length=150)
    user_name = models.CharField(max_length=100)
