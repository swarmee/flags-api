from flask_restplus import Namespace, Resource, fields, reqparse
from flask import make_response, send_file
import json

api = Namespace('entity', description='Entity Type End Points')

validEntityCodes = ['b', 'm', 'f']

api_params = api.parser()
# Look only in the querystring
api_params.add_argument('format',
                        required=False,
                        location='args',
                        help='lower case svg or png')


##### Simple Entity Type to Graphic API
@api.route('/code/<entitycode>')
class countryFlag(Resource):
    @api.expect(api_params)
    def get(self, entitycode):
        args = api_params.parse_args()
        fileType = args['format']
        if fileType is None or fileType not in ['png', 'svg']:
            fileType = 'png'
        entityCode = entitycode.lower()
        if entityCode not in validEntityCodes:
            entityCode = 'u'
            fileType = 'png'
        res = make_response(
            send_file('./images/entity_types/' + entityCode + '.' + fileType,
                      attachment_filename=entityCode + '.' + fileType,
                      as_attachment=False,
                      add_etags=False,
                      cache_timeout=0))
        res.headers['Access-Control-Allow-Origin'] = "*"
        return res
