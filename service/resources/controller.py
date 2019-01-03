from flask_restful import Resource, reqparse
from service.models.controller import ControllerModel
from flask_jwt import jwt_required


class Controller(Resource):
    """
    JSON
    {
        "name": name
        "range":  - range of controller
        "value": - retrieved or to be set
        "unit": - unit
    }
    """
    parser = reqparse.RequestParser()
    parser.add_argument('set_value',
                        type=int,
                        required=True,
                        help='This field must be specified!'
                        )
    parser.add_argument('range',
                        type=int,
                        required=True,
                        help='Integer range of controller.')
    parser.add_argument('unit',
                        type=str,
                        required=True,
                        help='Unit of controller.')
    parser.add_argument('cluster_id',
                        type=int,
                        required=True,
                        help='Every controller needs a cluster id.')

    @jwt_required()
    def get(self, name):
        controller = ControllerModel.find_by_name(name)
        if controller:
            return controller.json()
        return {'message': 'Controller {} not found'.format(name)}, 404

    def post(self, name):
        if ControllerModel.find_by_name(name):
            return {'message': 'Controller {} already exitsts'.format(name)}, 400

        data = Controller.parser.parse_args()

        controller = ControllerModel(name, **data)

        try:
            controller.save_to_db()
        except Exception:
            return {'message': 'An error occured inserting the controller'}, 500

        return controller.json(), 201

    def put(self, name):
        data = Controller.parser.parse_args()

        controller = ControllerModel.find_by_name(name)

        if controller is None:
            controller = ControllerModel(name, **data)
        else:
            controller.set_value = data['set_value']
            controller.range = data['range']
            controller.unit = data['unit']
        controller.save_to_db()

        return controller.json()

    def delete(self, name):
        controller = ControllerModel.find_by_name(name)
        if controller:
            controller.delete_from_db()


# @jwt_required
class ControllerCollection(Resource):
    def get(self):
        return {'controllers': [controller.json() for controller in ControllerModel.query.all()]}
