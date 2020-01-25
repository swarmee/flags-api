from flask_restplus import Namespace, Resource, fields, reqparse
from flask import make_response, send_file
import json

api = Namespace('payment_network',
                description='Payment Network Graphic End Points')

validNetworkNames = [
    "swift", "alipay", "currencyFair", "hifx", "moneyGram", "ofx", "paypal",
    "transFast", "transferWise", "westernUnion"
]

api_params = api.parser()
# Look only in the querystring
api_params.add_argument('format',
                        required=False,
                        location='args',
                        help='lower case svg or png')


##### Simple Network to Graphic API
@api.route('/name/<networkname>')
class countryFlag(Resource):
    @api.expect(api_params)
    def get(self, networkname):
        args = api_params.parse_args()
        fileType = args['format']
        if fileType is None or fileType not in ['png', 'svg']:
            fileType = 'png'
        networkName = networkname.lower()
        if networkName not in validNetworkNames:
            networkName = 'unknown'
            fileType = 'png'
        res = make_response(
            send_file('./images/payment_network/' + networkName + '.' +
                      fileType,
                      attachment_filename=networkName + '.' + fileType,
                      as_attachment=False,
                      add_etags=False,
                      cache_timeout=0))
        res.headers['Access-Control-Allow-Origin'] = "*"
        return res
