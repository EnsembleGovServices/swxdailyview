import os
from collections import Counter

from datetime import datetime, timedelta

from SWx_Dailly_View_Project.kp_forecast.utils import formatted_data_fetch

ACCESS_KEY = os.getenv("ACCESS_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
BUCKET_NAME = os.getenv("BUCKET_NAME")


class GetTodayKpService:

    @staticmethod
    def kp_rate_today():
        file_date, formatted_data = formatted_data_fetch()
        kp_rates_output = [data['kp'] for data in formatted_data if data['time_tag'].split(" ", 1)[0] == file_date]
        kp_rate_dict = dict(Counter(kp_rates_output))
        max_kp_occurrence = max(kp_rate_dict, key=kp_rate_dict.get)
        return max_kp_occurrence

    @staticmethod
    def time_interval_kp_rate(rate):

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
    def kp_rate_as_per_intervals():
        file_date, formatted_data = formatted_data_fetch()

        kp_rate_as_per_intervals_list = [
            GetTodayKpService.time_interval_kp_rate(i) for i in formatted_data
            if i['time_tag'].split(" ", 1)[0] == file_date
        ]

        return kp_rate_as_per_intervals_list

    @staticmethod
    def predicted_kp_index():

        file_date, formatted_data = formatted_data_fetch()

        predicted_data = [data for data in formatted_data if data['observed'] == 'predicted']

        date_time_obj = datetime.strptime(file_date + ' 00:00:00', '%Y-%m-%d %H:%M:%S')

        next_one_day = date_time_obj + timedelta(days=1)
        next_sec_day = date_time_obj + timedelta(days=2)
        next_third_day = date_time_obj + timedelta(days=3)

        next_three_dates = [str(next_one_day).split(" ", 1)[0],
                            str(next_sec_day).split(" ", 1)[0],
                            str(next_third_day).split(" ", 1)[0]]
        predicted_next_three_days_kp = []
        for observed_predicted_dates in predicted_data:
            if observed_predicted_dates['time_tag'].split(" ", 1)[0] in next_three_dates:
                predicted_next_three_days_kp.append(observed_predicted_dates['kp'])

        return max(predicted_next_three_days_kp)
