from collections import Counter

from datetime import datetime, timedelta
from http import HTTPStatus

from flask import request

from SWx_Dailly_View_Project import cache
from SWx_Dailly_View_Project.constants import FILE_NOT_FETCHED
from SWx_Dailly_View_Project.kp_forecast.utils import formatted_data_fetch, convert_timestamp_to_file_name
from SWx_Dailly_View_Project.languages import Response


class GetTodayKpService:

    @staticmethod
    @cache.memoize(timeout=600)
    def kp_rate_today():
        """
            Finds Today Kp index with its noaa_scale value
            :param : None
            :return: if GET data is correct then instance data or else gives error message
                    [ o/p includes kp_index & noaa_scale value ]
        """
        if request.args.get('time_stamp'):
            time_stamp = int(request.args.get('time_stamp'))
        else:
            time_stamp = datetime.now().timestamp()

        file_name = convert_timestamp_to_file_name(time_stamp)
        if not formatted_data_fetch(file_name):
            return Response(status_code=HTTPStatus.BAD_REQUEST,
                            message=FILE_NOT_FETCHED).send_error_response()
        file_date, formatted_data = formatted_data_fetch(file_name)
        kp_rates_output = [data['kp'] for data in formatted_data if data['time_tag'].split(" ", 1)[0] == file_date]
        kp_rate_dict = dict(Counter(kp_rates_output))
        response = {'kp_index': max(kp_rate_dict, key=kp_rate_dict.get)}
        kp_index = float(response['kp_index'])
        if kp_index >= float(5):
            if kp_index == float(5):
                response['noaa_scale'] = 'G1'
            elif kp_index == float(6):
                response['noaa_scale'] = 'G2'
            elif kp_index == float(7):
                response['noaa_scale'] = 'G3'
            elif kp_index == float(8):
                response['noaa_scale'] = 'G4'
            elif kp_index == float(9):
                response['noaa_scale'] = 'G5'
        else:
            response['noaa_scale'] = None
        return response

    @staticmethod
    def time_interval_kp_rate(rate):
        """
            Converts the csv data into interval
        """

        time_interval = rate['time_tag'].split(":", 1)[0]
        if time_interval.split(" ", 1)[1] == "00":
            return {"00-03":
                {
                    "kp": rate['kp'],
                    "noaa_scale": rate['noaa_scale']
                }
            }
        elif time_interval.split(" ", 1)[1] == "03":
            return {"03-06":
                {
                    "kp": rate['kp'],
                    "noaa_scale": rate['noaa_scale']
                }
            }
        elif time_interval.split(" ", 1)[1] == "06":
            return {"06-09":
                {
                    "kp": rate['kp'],
                    "noaa_scale": rate['noaa_scale']
                }
            }
        elif time_interval.split(" ", 1)[1] == "09":
            return {"09-12":
                {
                    "kp": rate['kp'],
                    "noaa_scale": rate['noaa_scale']
                }
            }
        elif time_interval.split(" ", 1)[1] == "12":
            return {"12-15":
                {
                    "kp": rate['kp'],
                    "noaa_scale": rate['noaa_scale']
                }
            }
        elif time_interval.split(" ", 1)[1] == "15":
            return {"15-18":
                {
                    "kp": rate['kp'],
                    "noaa_scale": rate['noaa_scale']
                }
            }
        elif time_interval.split(" ", 1)[1] == "18":
            return {"18-21":
                {
                    "kp": rate['kp'],
                    "noaa_scale": rate['noaa_scale']
                }
            }
        elif time_interval.split(" ", 1)[1] == "21":
            return {"21-00":
                {
                    "kp": rate['kp'],
                    "noaa_scale": rate['noaa_scale']
                }
            }

    @staticmethod
    @cache.memoize(timeout=600)
    def kp_rate_as_per_intervals():
        """
            fetch kp rates as per intervals
        """
        if request.args.get('time_stamp'):
            time_stamp = int(request.args.get('time_stamp'))
        else:
            time_stamp = datetime.now().timestamp()

        file_name = convert_timestamp_to_file_name(time_stamp)

        if not formatted_data_fetch(file_name):
            return Response(status_code=HTTPStatus.BAD_REQUEST,
                            message=FILE_NOT_FETCHED).send_error_response()

        file_date, formatted_data = formatted_data_fetch(file_name)

        return [GetTodayKpService.time_interval_kp_rate(i) for i in formatted_data if
                i['time_tag'].split(" ", 1)[0] == file_date]

    @staticmethod
    @cache.memoize(timeout=600)
    def predicted_kp_index():
        """
            finds the highest predicted kp index rate value for next 3 days
        """
        if request.args.get('time_stamp'):
            time_stamp = int(request.args.get('time_stamp'))
        else:
            time_stamp = datetime.now().timestamp()

        file_name = convert_timestamp_to_file_name(time_stamp)
        if not formatted_data_fetch(file_name):
            return Response(status_code=HTTPStatus.BAD_REQUEST,
                            message=FILE_NOT_FETCHED).send_error_response()

        file_date, formatted_data = formatted_data_fetch(file_name)

        predicted_data = [data for data in formatted_data if data['observed'] == 'predicted']

        date_time_obj = datetime.strptime(f'{file_date} 00:00:00', '%Y-%m-%d %H:%M:%S')

        next_one_day = date_time_obj + timedelta(days=1)
        next_sec_day = date_time_obj + timedelta(days=2)
        next_third_day = date_time_obj + timedelta(days=3)

        next_three_dates = [str(next_one_day).split(" ", 1)[0],
                            str(next_sec_day).split(" ", 1)[0],
                            str(next_third_day).split(" ", 1)[0]]
        predicted_next_three_days_kp = [observed_predicted_dates['kp'] for observed_predicted_dates in predicted_data if
                                        observed_predicted_dates['time_tag'].split(" ", 1)[0] in next_three_dates]
        highest_predicted_kp_index = float(max(predicted_next_three_days_kp))
        if highest_predicted_kp_index >= float(5):
            if highest_predicted_kp_index == float(5):
                noaa_scale = 'G1'
            elif highest_predicted_kp_index == float(6):
                noaa_scale = 'G2'
            elif highest_predicted_kp_index == float(7):
                noaa_scale = 'G3'
            elif highest_predicted_kp_index == float(8):
                noaa_scale = 'G4'
            elif highest_predicted_kp_index == float(9):
                noaa_scale = 'G5'
        else:
            noaa_scale = None
        return {'highest_predicted_kp_index': max(predicted_next_three_days_kp),
                'noaa_scale': noaa_scale
                }
