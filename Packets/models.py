from django.db import models
# from Reviews.models import Rating, Comment





class Packet(models.Model):
    season = models.CharField(max_length=20)
    title = models.CharField(max_length=250)
    image = models.ForeignKey('PacketImage', on_delete=models.CASCADE, related_name='packets')
    price = models.IntegerField()
    description = models.TextField()
    transport = models.CharField(max_length=250)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    free_places = models.IntegerField()
    packets_rating = models.ForeignKey('Reviews.Rating', on_delete=models.CASCADE, related_name='packetrating')
    packets_comments = models.ForeignKey('Reviews.Comment', on_delete=models.CASCADE, related_name='packets')
    in_stock = models.BooleanField()
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.title}, {self.season}" 

class PacketImage(models.Model):
    packet = models.ForeignKey(Packet, on_delete=models.CASCADE, related_name='images')
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='media/packet_image/')
    created_at = models.DateTimeField(auto_now_add=True)
    udated_at = models.DateTimeField(auto_now=True)

    
class Hotel(models.Model):
    title = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    address = models.CharField(max_length=255)
    hotels_rating = models.IntegerField()
    season = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title}, {self.country}" 



    
