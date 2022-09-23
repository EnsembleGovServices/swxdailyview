from flask import Blueprint
from flask_restful import Api

from SWx_Dailly_View_Project.goes_proton_flux import resources

# lets creates the flask blueprint for this PROTON-FLUX-DATA related api
proton_flux_blueprint = Blueprint('proton_flux_blueprint', __name__)
proton_flux_api = Api(proton_flux_blueprint)

# Add get_proton_flux_data resource to the api
proton_flux_api.add_resource(resources.GetProtonFluxResource, '/get-proton-flux-data')
