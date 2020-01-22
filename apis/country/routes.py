from flask_restplus import Namespace, Resource, fields, reqparse
from flask import make_response, send_file
import json

with open('./resources/country_code_list.json') as f:
    validCountryCodes = json.load(f)

api = Namespace('country', description='Country Flags End Points')

api_params = api.parser()
# Look only in the querystring
api_params.add_argument('format',
                        required=False,
                        location='args',
                        help='lower case svg or png')


##### Simple ISO 2 Letter Country Code to Map
@api.route('/code/<countryCode>')
class countryFlag(Resource):
    @api.expect(api_params)
    def get(self, countryCode):
        args = api_params.parse_args()
        fileType = args['format']
        if fileType is None or fileType not in ['png', 'svg']:
            fileType = 'png'
        countryCode = countryCode.lower()
        if countryCode not in validCountryCodes:
            countryCode = 'unknown'
            fileType = 'jpeg'
        res = make_response(
            send_file('./images/country_flags/' + countryCode + '.' + fileType,
                      attachment_filename=countryCode + '.' + fileType,
                      as_attachment=True,
                      add_etags=False,
                      cache_timeout=0))
        res.headers['Access-Control-Allow-Origin'] = "*"
        return res
