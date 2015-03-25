import shapefile

sf = shapefile.Reader("shapefiles/Estructuras_Abandonadas")

shapes = sf.shapes()
len(shapes)


fields = sf.fields