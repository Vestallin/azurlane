from display.models import Ship
import csv


def run():
    with open("./ALStatV2.csv", encoding="ISO-8859-1") as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Ship.objects.all().delete()

        for row in reader:
            row = [0 if x in ["??", ""] else x for x in row]
            film = Ship(
                sid=row[0],
                ship_name=row[1],
                rarity=row[2],
                faction=row[3],
                class_name=row[4],
                lck=row[5],
                armor=row[6],
                spd=row[7],
                hp=row[8],
                fp=row[9],
                aa=row[10],
                trp=row[11],
                eva=row[12],
                avi=row[13],
                oil=row[14],
                rld=row[15],
                asw=row[16],
                oxy=row[17],
                ammo=row[18],
                acc=row[19],
            )
            film.save()
