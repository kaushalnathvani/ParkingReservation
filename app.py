from flask import Blueprint
from flask_restful import Api
import sys
sys.path.append('resources')
from ViewParkingSpots import ViewParkingSpots
from ReserveSpot import ReserveSpot
from CancelReservation import CancelReservation
from SearchSpot import SearchSpot
from ValidateNumber import ValidateNumber

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(ViewParkingSpots, '/ViewParkingSpots')
api.add_resource(ReserveSpot, '/ReserveSpot/<id>')
api.add_resource(CancelReservation, '/CancelReservation/<id>')
api.add_resource(SearchSpot, '/SearchSpot/<address>')
api.add_resource(ValidateNumber, '/ValidateNumber/<phone_number>')
