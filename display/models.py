from django.db import models

# Create your models here.
class Ship(models.Model):
    ship_name = models.CharField(max_length=255)
    class_name = models.CharField(max_length=10)
    sid = models.CharField(max_length=10, verbose_name="Ship ID")
    hp = models.IntegerField(default=0)
    fp = models.IntegerField(default=0)
    trp = models.IntegerField(default=0)
    avi = models.IntegerField(default=0)
    aa = models.IntegerField(default=0)
    rld = models.IntegerField(default=0)
    eva = models.IntegerField(default=0)
    spd = models.IntegerField(default=0)
    acc = models.IntegerField(default=0)
    lck = models.IntegerField(default=0)
    asw = models.IntegerField(default=0)
    oil = models.IntegerField(default=0)
    oxy = models.IntegerField(default=0)
    ammo = models.IntegerField(default=0)
    faction = models.CharField(max_length=20)
    armor = models.CharField(max_length=10)
    rarity = models.CharField(max_length=15)