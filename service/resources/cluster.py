from flask_restful import Resource
from service.models.cluster import ClusterModel


class Cluster(Resource):
    def get(self, name):
        cluster = ClusterModel.find_by_name(name)
        if cluster:
            return cluster.json()
        return {'message': 'Cluster not found'}, 404

    def post(self, name):
        if ClusterModel.find_by_name(name):
            return {'message': 'Cluster {} already exists'.format(name)}, 400

        cluster = ClusterModel(name)
        try:
            cluster.save_to_db()
        except:
            return {'message': 'An error occurred while creating the cluster.'}, 500

        return cluster.json(), 201

    def delete(self, name):
        cluster = ClusterModel.find_by_name(name)
        if cluster:
            cluster.delete_from_db()

        return {'message': 'Cluster deleted.'}


class ClusterCollection(Resource):
    def get(self):
        return {'clusters': [cluster.json() for cluster in ClusterModel.query.all()]}
