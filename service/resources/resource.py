from flask_restful import Resource, reqparse
from service.models.controller import ControllerModel
from flask_jwt import jwt_required
from flask import request
import sqlite3

sensors = []


# @jwt_required
class Sensor(Resource):
    """
    This only retrieves the data from DB
    """

    def get(self, name):
        for sensor in sensors:
            if sensor['name'] == name:
                return sensor
        return {'message': 'Sensor {} not found'.format(name)}, 404


# @jwt_required
class SensorCollection(Resource):
    """
    This only retrieves the data from the DB
    """

    def get(self):
        return {'message': "All sensors json will be here"}


# @jwt_required


# @jwt_required
class ConfigSensor(Resource):
    def get(self, name):
        return {'name': name}

    def post(self, name):
        return


# @jwt_required
class Config(Resource):
    def get(self):
        return {'message': 'Config will be returned'}
