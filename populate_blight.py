import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blight_project.settings')

import django
django.setup()

from blight_app.models import AbndSite
import csv



def populate():
    with open('inventario.csv', 'rb') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            try:
                add_prop(catastro=str(row[3]),
                         tenencia=str(row[4]),
                         calificacion=str(row[12]),
                         calle=str(row[8]),
                         comunidad=str(row[9]))

                # Print out what we have added to the user.
                for abn in AbndSite.objects.all():
                    print str(abn)
            except:
                pass
                
def add_prop(catastro, tenencia, calificacion, calle, comunidad):
    abn = AbndSite.objects.get_or_create(catastro=catastro, tenencia=tenencia,
                                         calificacion=calificacion, calle=calle,
                                         comunidad=comunidad)[0]
    return abn

# Start execution here!
if __name__ == '__main__':
    print "Starting Blight population script..."
    populate()