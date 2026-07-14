import logging
from datetime import datetime
import functions_framework
from flask import jsonify, make_response


logger = logging.getLogger('travel_booking_fucntion')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(
    logging.Formatter('%(asctime)s %(levelname)s %(name)s: %(message)s')
)

if not logger.handlers:
    logger.addHandler(handler)

@functions_framework.http
def travel_booking(request):
    logger.info('Applciation Start Complete')

    return 'Application Exit'