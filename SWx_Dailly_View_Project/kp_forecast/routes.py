from flask import Blueprint
from flask_restful import Api

from SWx_Dailly_View_Project.kp_forecast.resources import GetKpData, GetIntervalKpData, GetHighestKpInNextThreeDays, \
    Root

kp_blueprint = Blueprint('kp_blueprint', __name__)
kp_service_rest_api = Api(kp_blueprint)

# kp blueprint routes add resources
kp_service_rest_api.add_resource(Root, '/')
kp_service_rest_api.add_resource(GetKpData, '/current-kp-index')
kp_service_rest_api.add_resource(GetIntervalKpData, '/get-interval-kp-data')
kp_service_rest_api.add_resource(GetHighestKpInNextThreeDays, '/predicted-kp-index')
