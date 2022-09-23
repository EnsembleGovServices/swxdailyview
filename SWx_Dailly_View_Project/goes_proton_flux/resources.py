from flask import request
from flask_restful import Resource

from SWx_Dailly_View_Project.goes_proton_flux import services


class GetProtonFluxResource(Resource):
    service_obj = services.GetProtonFluxService()

    @classmethod
    def get(cls):
        """
            Fetch Goes Proton Flux data
            [ including options for ( 6 Hours, 1 day, 3 days, 7 days )
            :param : --> request Hours & days (respectively) ]
            :return: if GET data is correct then instance data or else gives error message
        """
        return cls.service_obj.proton_flux_data(request)
