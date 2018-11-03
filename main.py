from flask_api import FlaskAPI

app = FlaskAPI(__name__)

@app.route('/example/')
def example():
    return {'hello': 'world'}


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)