from flask import Flask

from blueprints.products_blueprints import products_blueprint
from blueprints.stores_blueprints import stores_blueprint


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

app.register_blueprint(products_blueprint)
app.register_blueprint(stores_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
