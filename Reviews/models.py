from django.db import models
from Packets.models import Packet
from account.models import User

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    body = models.TextField()
    packet = models.ForeignKey(Packet, on_delete=models.CASCADE, related_name='comment')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Rating(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rating')
    rating = models.IntegerField()
    packet = models.ForeignKey(Packet, on_delete=models.CASCADE, related_name='rating')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


