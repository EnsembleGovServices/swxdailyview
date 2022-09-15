from flask import request
from flask_restful import Resource

from SWx_Dailly_View_Project.goes_proton_flux import services


class GetProtonFluxResource(Resource):
    service_obj = services.GetProtonFluxService()

    @classmethod
    def get(cls):
        args = request.args
        return cls.service_obj.proton_flux_data(args)