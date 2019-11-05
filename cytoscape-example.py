import dash
import dash_cytoscape as cyto
import dash_html_components as html

app = dash.Dash(__name__)

terminal_nodes = [
    {
        'classes': 'terminal',
        'data': {
            'id': 'name',
            'label': 'name',
            'url': 'http://100.115.92.199:8080/v1/countryflag/au.png'
        }
    },
    {
        'classes': 'terminal',
        'data': {
            'id': 'abc',
            'label': 'abc',
            'url': 'http://100.115.92.199:8080/v1/countryflag/th.png'
        }
    },
    {
        'classes': 'terminal',
        'data': {
            'id': 'aaa',
            'label': 'aaa',
            'url': 'http://100.115.92.199:8080/v1/countryflag/th.png'
        }
    }
]

# Creating styles
stylesheet = [
    {
        'selector': '.terminal',
        'style': {
            'width': 90,
            'height': 80,
            'background-fit': 'cover',
            'background-image': 'data(url)',
            'shape' : 'circle'
        }
    }
]


# Declare app layout
app.layout = html.Div([
    cyto.Cytoscape(
        id='cytoscape-images',
        layout={'name': 'cose'},
        style={'width': '100%', 'height': '550px'},
        stylesheet=stylesheet,
        elements=terminal_nodes 
    )
])

if __name__ == '__main__':
    app.run_server(debug=True,port=4000,threaded=True, host='0.0.0.0')
