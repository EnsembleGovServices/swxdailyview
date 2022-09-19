from flask_restful import Resource

from SWx_Dailly_View_Project.latitude_index.services import GetMidLatitudeResource, GetHighLatitudeResource


class GetMidLatitude(Resource):
    mid_latitude_obj = GetMidLatitudeResource()

    @classmethod
    def get(cls):
        return cls.mid_latitude_obj.get_mid_latitude()


class GetHighLatitude(Resource):
    high_latitude_obj = GetHighLatitudeResource()

    @classmethod
    def get(cls):
        return cls.high_latitude_obj.get_high_latitude()
