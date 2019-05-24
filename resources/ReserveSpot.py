from flask_restful import Resource, reqparse
from db_manager import DBManager
import sys
sys.path.append('models')
from models import ParkingSpots


class ReserveSpot(Resource):
    def get(self, id):

        resp = {'Booking Successful': False}
        print 'id:',id

        db_mgr = DBManager()
        session = db_mgr.get_session()

        results = []
        try:
            qry = session.query(ParkingSpots).filter(ParkingSpots.id == int(id)).update({'available': False})
            session.commit()

            qry = session.query(ParkingSpots.available).filter(ParkingSpots.id == int(id)).all()
            print qry
            if qry[0][0] == False:
                resp['Booking Successful'] = True
                resp['Your booking ID'] = id
        except Exception as e:
            print 'Error:',e
        finally:
            db_mgr.close_session(session)

        return resp
