from flask_restplus import Namespace, Resource, fields, reqparse
from flask import make_response, send_file
import json
import io
from PIL import Image, ImageDraw, ImageFont

api = Namespace('text2image', description='Convert Text to Image End Point')

api_params = api.parser()
# Look only in the querystring
api_params.add_argument('format',
                        required=False,
                        location='args',
                        help='lower case svg or png')


def create_image(imageText):
    img = Image.new('RGB', (25, 20), (255, 255, 255, 0))
    d = ImageDraw.Draw(img)
    imageText = imageText.upper()
    d.text((2, 0),
           imageText,
           fill=(10, 255, 0),
           align="center",
           font=ImageFont.truetype("./apis/text2image/Verdana.ttf", 16))
    # create file-object in memory
    file_object = io.BytesIO()
    # write PNG in file-object
    img.save(file_object, 'png')
    file_object.seek(0)
    return send_file(file_object,
                     mimetype='image/png',
                     attachment_filename=imageText + '.' + 'png',
                     as_attachment=False,
                     add_etags=False,
                     cache_timeout=0)


##### Simple Network to Graphic API
@api.route('/<imageText>')
class countryFlag(Resource):
    @api.expect(api_params)
    def get(self, imageText):
        args = api_params.parse_args()
        fileType = args['format']
        if fileType is None or fileType not in ['png', 'svg']:
            fileType = 'png'
        if len(imageText) > 2:
            imageText = imageText[0:2]
        image_file = create_image(imageText)
        res = make_response(image_file)
        res.headers['Access-Control-Allow-Origin'] = "*"
        return res
