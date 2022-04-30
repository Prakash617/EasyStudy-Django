from pyexpat import model

from django.db import models

# Create your models here.
SCHOOL_LEVEL = (
    ("Order Received", "Order Received"),
    ("Order Processing", "Order Processing"),
    ("On the way", "On the way"),
    ("Order Completed", "Order Completed"),
    ("Order Canceled", "Order Canceled"),
)

BACHELOR_LEVEL = (
    ("Order Received", "Order Received"),
    ("Order Processing", "Order Processing"),
    ("On the way", "On the way"),
    ("Order Completed", "Order Completed"),
    ("Order Canceled", "Order Canceled"),
)

MASTER_LEVEL = (
    ("Order Received", "Order Received"),
    ("Order Processing", "Order Processing"),
    ("On the way", "On the way"),
    ("Order Completed", "Order Completed"),
    ("Order Canceled", "Order Canceled"),
)

class School(model.Model):
    level = models.CharField(max_length=50, choices= SCHOOL_LEVEL)
    
    def __str__(self):
        return self.level