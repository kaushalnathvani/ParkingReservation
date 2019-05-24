from flask_restful import Resource, reqparse
import sys
sys.path.append('models')


class ValidateNumber(Resource):
    def get(self, phone_number):

        results = {'Valid': False}
        if len(phone_number) == 10:
            if phone_number[0] in ['7', '8', '9']:
                results['Valid'] = True

        return results

    def post(self):
        parser = reqparse.RequestParser()
        args = parser.parse_args()
        print args
        # results = {'Valid': False}
        # if len(phone_number) == 10:
        #     if phone_number[0] in ['7', '8', '9']:
        #         results['Valid'] = True
        #
        # return results
