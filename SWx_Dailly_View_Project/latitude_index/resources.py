from flask_restful import Resource

from SWx_Dailly_View_Project.latitude_index.services import GetMidLatitudeResource, GetHighLatitudeResource


class GetMidLatitude(Resource):
    mid_latitude_obj = GetMidLatitudeResource()

    @classmethod
    def get(cls):
        """
            Fetch Mid-latitude data with proper percentage wise data
            [ G1 -> minor, G2 -> moderate, G3 -> strong, G4 -> severe, G5 -> extreme ]
            :return: if GET data is correct then instance data or else gives error message
        """
        return cls.mid_latitude_obj.get_mid_latitude()


class GetHighLatitude(Resource):
    high_latitude_obj = GetHighLatitudeResource()

    @classmethod
    def get(cls):
        """
            Fetch High-latitude data with proper percentage wise data
            [ G1 -> minor, G2 -> moderate, G3 -> strong, G4 -> severe, G5 -> extreme ]
            :return: if GET data is correct then instance data or else gives error message
        """
        return cls.high_latitude_obj.get_high_latitude()
