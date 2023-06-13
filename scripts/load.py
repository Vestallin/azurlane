from display.models import Ship
import csv


def run():
    with open('./ALStats.csv', encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Ship.objects.all().delete()

        for row in reader:
            row = [0 if x in ["??", ""]  else x for x in row]
            film = Ship(ship_name=row[2], class_name=row[1], sid=row[0], hp=row[4],
                        rarity=row[3], fp=row[5], trp=row[6], avi=row[7], aa=row[8],
                        rld=row[9], eva=row[10], armor=row[11], spd=row[12], acc=row[13], lck=row[14],
                        asw=row[15], oil=row[16], oxy=row[17], ammo=row[18], faction=row[19],
                        )
            film.save()