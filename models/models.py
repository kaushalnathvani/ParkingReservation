from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ParkingSpots(Base):
    __tablename__ = 'parking_spots'

    id = Column(Integer(), primary_key=True)
    available = Column(Boolean())
    lat = Column(Float())
    lon = Column(Float())
    address = Column(String())
    cost = Column(Float())

    def toJSON(self):

        json = {
            'id': self.id,
            'available': self.available,
            'lat': self.lat,
            'lon': self.lon,
            'address': self.address,
            'cost': self.cost
        }

        return json