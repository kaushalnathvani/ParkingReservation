from flask_restful import Resource, reqparse
from db_manager import DBManager
import sys
sys.path.append('models')
from models import ParkingSpots
import geopy.distance


class SearchSpot(Resource):
    def get(self, address):

        db_mgr = DBManager()
        session = db_mgr.get_session()

        if len(address.split(',')) < 3:
            return '{"Invalid data format"}'

        lat, lon, radius = address.split(',')

        coords_1 = (lat, lon)

        results = []
        temp = []
        try:
            data_list = session.query(ParkingSpots).filter(ParkingSpots.available == True)

            for data in data_list:
                temp.append(data.toJSON())

            for rec in temp:

                print 'rec:',rec
                coords_2 = (rec['lat'], rec['lon'])

                dist = geopy.distance.vincenty(coords_1, coords_2).meters
                print 'dist:',dist

                if dist < float(radius):
                    results.append(rec)
        except Exception as e:
            print 'Error:',e
        finally:
            db_mgr.close_session(session)

        return results
