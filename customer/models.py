import datetime

from django.db import models
from owner.models import Books
from django.contrib.auth.models import User
# Create your models here.
class Carts(models.Model):
    product=models.ForeignKey(Books,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    qty=models.PositiveIntegerField(default=1)
    options=(
        ("incart","incart"),
        ("orderplaced","orderplaced"),
        ("ordercancelled","ordercancelled")
    )
    status=models.CharField(max_length=20,choices=options,default="incart")

class Orders(models.Model):
    product=models.ForeignKey(Books,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    edate=datetime.timedelta(days=5)
    expected_delivery_date=models.DateField(default=edate)
    options=(
        ("order_placed","order_placed"),
        ("dispatched","dispatched"),
        ("in_transit","in_transit"),
        ("delivered","delivered"),
        ("oreder_cancelled","oreder_cancelled"),
    )
    status=models.CharField(max_length=20,choices=options,default="order_placed")
