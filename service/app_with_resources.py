from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from service.resources.controller import Controller, ControllerCollection
from service.resources.cluster import Cluster, ClusterCollection
from service.security import authenticate, identity
from service.resources.user import UserRegister

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'iot'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authentication_handler=authenticate, identity_handler=identity)

api.add_resource(UserRegister, '/register')
#api.add_resource(Config, '/api/config')
#api.add_resource(ConfigSensor, '/api/config/sensors/<name>')
api.add_resource(ControllerCollection, '/api/config/controllers')
api.add_resource(Controller, '/api/config/controllers/<name>')
api.add_resource(ClusterCollection, '/api/clusters')
api.add_resource(Cluster, '/api/clusters/<name>')
#api.add_resource(Sensor, '/api/sensors/<name>')
#api.add_resource(SensorCollection, '/api/sensors')


if __name__ == '__main__':
    from service.db import db
    db.init_app(app)
    app.run(host='127.0.0.1', port=5000)
