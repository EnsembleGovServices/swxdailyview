from flask_restful import Resource

from SWx_Dailly_View_Project.kp_forecast import services


class Root(Resource):
    @classmethod
    def get(cls):
        """
            CHECK weather the root server is running correctly or not.
        """
        return {'status': 'OK'}


class GetKpData(Resource):
    service_obj = services.GetTodayKpService()

    @classmethod
    def get(cls):
        """
            Fetch Today Kp index with its noaa_scale value
            :param : None
            :return: if GET data is correct then instance data or else gives error message
                    [ o/p includes kp_index & noaa_scale value ]
        """
        return cls.service_obj.kp_rate_today()


class GetIntervalKpData(Resource):
    service_obj = services.GetTodayKpService()

    @classmethod
    def get(cls):
        """
            Fetch Today Kp index rates with particular intervals
            Here we have [ 00-03-06-09-12-15-18-21 intervals ]
            :param : None
            :return: if GET data is correct then instance data or else gives error message
                    [ o/p includes interval kp_index with noaa_scale value ]
        """
        return cls.service_obj.kp_rate_as_per_intervals()


class GetHighestKpInNextThreeDays(Resource):
    service_obj = services.GetTodayKpService()

    @classmethod
    def get(cls):
        """
            Fetch predicted highest kp_index value for next 3 days
            :param : None
            :return: if GET data is correct then instance data or else gives error message
                    [ o/p includes kp_index value --> str format]
        """
        return cls.service_obj.predicted_kp_index()
