from flask_restful import Resource
from db_manager import DBManager
import sys
sys.path.append('models')
from models import ParkingSpots


class ViewParkingSpots(Resource):
    def get(self):

        db_mgr = DBManager()
        session = db_mgr.get_session()

        results = []
        try:
            data_list = session.query(ParkingSpots)

            for data in data_list:
                results.append(data.toJSON())
        except Exception as e:
            print 'Error:',e
        finally:
            db_mgr.close_session(session)

        return results
