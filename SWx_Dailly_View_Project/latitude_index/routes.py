from flask import Blueprint
from flask_restful import Api

from SWx_Dailly_View_Project.latitude_index.resources import GetMidLatitude, GetHighLatitude

latitude_blueprint = Blueprint('latitude_blueprint', __name__)
latitude_rest_api = Api(latitude_blueprint)

# latitude blueprint routes for mid and high respectively
latitude_rest_api.add_resource(GetMidLatitude, '/get-mid-latitude')
latitude_rest_api.add_resource(GetHighLatitude, '/get-high-latitude')
