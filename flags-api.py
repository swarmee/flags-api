# gunicorn3 static-app:app.server --bind=0.0.0.0:8080 --workers=1 --reload
from   flask import Flask, request, request, send_file, make_response
import json
from   flask_restplus import Api, Resource, fields, abort
from   werkzeug.contrib.fixers import ProxyFix

with open('./country_code_list.json') as f:
  validCountryCodes = json.load(f)

app = Flask(__name__, static_url_path='/images',static_folder='images')
app.config.SWAGGER_UI_DOC_EXPANSION = 'full'
app.config.SWAGGER_UI_OPERATION_ID = True
app.config.SWAGGER_UI_REQUEST_DURATION = True
api = Api(app,
          version='1.0', 
          title='World Flags API', 
          description='Provide a country code get a flag', 
          prefix="/v1",
          contact="john@swarmee.net",
          contact_url="www.swarmee.net"
         # ,          doc='/doc/'
         )
app.wsgi_app = ProxyFix(app.wsgi_app)

ns = api.namespace('countryflag', description='country flag name space')


##### Simple ISO 2 Letter Country Code to Map
@ns.route('/<countryCode>.<fileType>')
class countryFlag(Resource):
  #@ns.produces(['image/png'])
  def get(self,countryCode, fileType):
    countryCode = countryCode.lower()
    fileType    = fileType.lower()
    if countryCode not in validCountryCodes:
        countryCode = 'unknown'
        fileType = 'jpeg'
    res = make_response(send_file('./images/' + countryCode + '.'+ fileType, 
                                  attachment_filename=countryCode +'.'+ fileType,
                                  as_attachment=True,
                                  add_etags=False,
                                  cache_timeout=0)  )
    res.headers['Access-Control-Allow-Origin'] =  "*"
    return res 

if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0', 
            port=8080,
            threaded=True)