from flask import Flask
from apis import api

app = Flask(__name__, static_url_path='/images', static_folder='images')

#app.config.SWAGGER_UI_DOC_EXPANSION = 'full'
app.config.SWAGGER_UI_OPERATION_ID = True
app.config.SWAGGER_UI_REQUEST_DURATION = True

api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, port=8080, host="0.0.0.0", threaded=True)
