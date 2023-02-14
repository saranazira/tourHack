from django.db import models
from Packets.models import Packet


class Payment(models.Model):
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    payment_packet = models.ForeignKey(Packet, on_delete=models.CASCADE, related_name='payment')
    payment_tickets = models.CharField(max_length=250)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)#price*nmb
    status = models.ForeignKey('Status', on_delete=models.CASCADE)
    comments = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"{self.customer_email}, {self.nmb}"


class Ticket(models.Model):
    info = models.CharField(max_length=255)
    ticket_payments = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='ticket')
    

class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'
