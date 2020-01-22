from flask_restplus import Namespace, Resource, fields, reqparse
from flask import make_response, send_file
import json

api = Namespace('identification', description='Identification Type End Points')

validIdentificationCodes = ['asic', 'd', 'dob']

api_params = api.parser()
# Look only in the querystring
api_params.add_argument('format',
                        required=False,
                        location='args',
                        help='lower case svg or png')


##### Simple Entity Type to Graphic API
@api.route('/code/<identificationcode>')
class countryFlag(Resource):
    @api.expect(api_params)
    def get(self, identificationcode):
        args = api_params.parse_args()
        fileType = args['format']
        if fileType is None or fileType not in ['png', 'svg']:
            fileType = 'png'
        identificationCode = identificationcode.lower()
        if identificationCode not in validIdentificationCodes:
            entityCode = 'u'
            fileType = 'png'
        res = make_response(
            send_file('./images/identification_types/' + identificationCode +
                      '.' + fileType,
                      attachment_filename=identificationCode + '.' + fileType,
                      as_attachment=False,
                      add_etags=False,
                      cache_timeout=0))
        res.headers['Access-Control-Allow-Origin'] = "*"
        return res
