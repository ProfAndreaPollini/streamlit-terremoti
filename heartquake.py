"""
modulo del modello di terremoto utilizzato nella applicazione
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Heartquake:
    """Un terremoto"""
    
    magnitude: float
    place: str
    timestamp: datetime
    lat: float
    lon: float
    z: float


    @staticmethod
    def from_feature(feature):
        print(type(feature["properties"]["updated"]))
        magnitude = feature["properties"]["mag"]
        place = feature["properties"]["place"]
        timestamp = datetime.now()#fromtimestamp(float(feature["properties"]["updated"]))
        lat = feature["geometry"]["coordinates"][1]
        lon = feature["geometry"]["coordinates"][0]
        z = feature["geometry"]["coordinates"][2]

        return Heartquake(magnitude=magnitude, place=place, timestamp=timestamp, lat=lat, lon=lon, z=z)
