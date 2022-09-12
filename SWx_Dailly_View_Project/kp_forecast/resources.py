from flask_restful import Resource

from SWx_Dailly_View_Project.kp_forecast import services


class GetKpData(Resource):
    service_obj = services.GetTodayKpService()

    @classmethod
    def get(cls):
        return cls.service_obj.kp_rate_today()


class GetIntervalKpData(Resource):
    service_obj = services.GetTodayKpService()

    @classmethod
    def get(cls):
        return cls.service_obj.kp_rate_as_per_intervals()


class GetHighestKpInNextThreeDays(Resource):
    service_obj = services.GetTodayKpService()

    @classmethod
    def get(cls, desired_date):
        return cls.service_obj.predicted_kp_index(desired_date)
