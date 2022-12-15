from flask_restful import Resource

from SWx_Dailly_View_Project.solar_wind_speed.services import GetSolarWindSpeedService


class GetSolarWindSpeedResources(Resource):
    get_solar_wind_speed_obj = GetSolarWindSpeedService()

    @classmethod
    def get(cls):
        """
            Fetch solar wind speed
            :return: if GET data is correct then instance data or else gives error message
        """
        return cls.get_solar_wind_speed_obj.get_solar_wind_speed()
