from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    price = models.PositiveIntegerField()
    purchased = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
