from flask import Blueprint
from flask_restful import Api

from SWx_Dailly_View_Project.solar_wind_speed.resources import GetSolarWindSpeedResources

solar_wind_blueprint = Blueprint('solar_wind_blueprint', __name__)
solar_wind_rest_api = Api(solar_wind_blueprint)


# solar wind routes for GET solar wind speed data
solar_wind_rest_api.add_resource(GetSolarWindSpeedResources, '/get-solar-wind-speed')