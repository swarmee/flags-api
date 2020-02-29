from flask_restx import Api
from apis.country import *
from apis.entity import *
from apis.payment_network import *
from apis.identification import *
from apis.text2image import *

api = Api(
    version='1.0',
    title='Graphics APIs',
    description='Provide images to enhance analysis',
    prefix="/grayling/v1",
    #          contact="john@swarmee.net",
    #          contact_url="www.swarmee.net"
    # ,          doc='/doc/'
)

api.add_namespace(entity, path='/entity')
api.add_namespace(country, path='/country')
api.add_namespace(identification, path='/identification')
api.add_namespace(payment_network, path='/payment_network')
api.add_namespace(text2image, path='/text2image')