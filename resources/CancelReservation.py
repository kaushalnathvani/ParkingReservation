from flask_restful import Resource
from db_manager import DBManager
import sys
sys.path.append('models')
from models import ParkingSpots


class CancelReservation(Resource):
    def get(self, id):
        results = {'Cancellation Successful': False}

        db_mgr = DBManager()
        session = db_mgr.get_session()

        try:
            qry = session.query(ParkingSpots).filter(ParkingSpots.id == int(id)).update({'available': True})
            session.commit()

            qry = session.query(ParkingSpots.available).filter(ParkingSpots.id == int(id)).all()
            print qry
            if qry[0][0] == True:
                results['Cancellation Successful'] = True
        except Exception as e:
            print 'Error:',e
        finally:
            db_mgr.close_session(session)

        return results
