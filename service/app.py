from flask import Flask, jsonify
from service.resources.resource import *


app = Flask(__name__)

# root
@app.route("/")
def index():
    """
    this is a root dir of my server
    :return: str
    """
    return "This is root!!!!"


@app.route('/api/sensors')
def api_sensors():
    """
    :return: list all defined sensors
    """
    return


@app.route('/api/sensors/<sensor_name>')
def api_sensor(sensor_name):
    """
    connect to the DB and fetch last row
    :param sensor_name:
    :return:
    """
    return 'sensor {}'.format(sensor_name)


@app.route('/users/<user>', methods=['GET'])
def hello_user(user):
    """
    this serves as a demo purpose
    :param user:
    :return: str
    """
    return "Hello %s!" % user


@app.route('/api/config')
def get_config():
    """
    GET /api/config - get whole configuration running on raspberry pi
    :return: json
    """
    # TODO: get config file shared with ext app or retrieve from DB
    pass


@app.route('/api/config/controllers')
def api_config_controllers():
    """
     GET /api/config/controllers
    :return: json
    """
    pass


@app.route('/api/config/controllers/<controller_name>', methods=['POST'])
def api_config_controller(controller_name):
    """
    POST /api/config/controllers/<controller_name>?range=<int>,unit=<str>
    define or edit controller, its range and unit on external app

    The request body must contain parameters in json:
    :param: range - max integer that can be set
    :param: unit - unit of the controller
    :return: json
    """
    pass


@app.route('/api/config/sensors/<sensor_name>', methods=['GET', 'POST'])
def api_config_sensor(sensor_name):
    """
    GET /api/config/sensors/<sensor_name> - get sensor related config like interval
    POST /api/config/sensors/<sensor_name>?interval=<int> - configure time interval, it controls how often the data is write to database
    :param: interval - in POST method sets the interval in seconds between two samples
    :param: other params that may be needed
    :return: json
    """
    pass


@app.route('/api/config/controllers/<controller_name>/tune')
def api_config_tune_controller(controller_name):
    """
    POST /api/config/controllers/<controller_name>/tune?direction=<up/down>,units=<int>
    eg. tune the temperature up of 2 C, default units=1, direction is required

    :param controller_name:
    :return:
    """
    pass


# POST
@app.route('/api/post_some_data', methods=['POST'])
def get_text_prediction():
    """
    predicts requested text whether it is ham or spam
    :return: json
    """
    json = request.get_json()
    print(json)
    if len(json['text']) == 0:
        return jsonify({'error': 'invalid input'})

    return jsonify({'you sent this': json['text']})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)