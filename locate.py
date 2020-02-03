import pandas
from geopy.geocoders import ArcGIS

def coordenadas(archivo):
    df=pandas.read_csv(archivo)
    try:
        if df.address.all:
            df.rename(columns={'address':'Address'},inplace=True)
    except:
        pass
    nom=ArcGIS()
    df["Coordinates"]= df["Address"].apply(nom.geocode)
    df["Latitude"]=df["Coordinates"].apply(lambda x:x.latitude if x != None else None)
    df["Longitude"]=df["Coordinates"].apply(lambda x:x.latitude if x != None else None)
    





        