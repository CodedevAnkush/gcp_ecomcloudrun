import logging
from datetime import datetime
import functions_framework
from flask import jsonify, make_response


logger = logging.getLogger('travel_booking_function')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(
    logging.Formatter('%(asctime)s %(levelname)s %(name)s: %(message)s')
)

if not logger.handlers:
    logger.addHandler(handler)

@functions_framework.http
def travel_booking_cicd(request):
    request_json = request.get_json(silent=True)
    request_args = request.args

    logger.info('Applciation Start Complete')

    logger.info('Extracting name from request')
    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'

    logger.info('Name extract process completed.')

    logger.info( 'Application Exit')
    return f"Hello {name}!"
  

    