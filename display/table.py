# display/tables.py
import django_tables2 as tables
from .models import Ship
class ShipTable(tables.Table):
    class Meta:
        model = Ship
        fields = ("sid", "ship_name", "class_name", "rarity", "hp", "fp", "trp", "avi", "aa", "rld", "eva", "spd", "acc",
                  "lck", "asw", "oil", "oxy", "ammo", "faction", "armor", )
