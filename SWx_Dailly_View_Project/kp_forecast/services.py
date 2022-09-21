from collections import Counter

from datetime import datetime, timedelta

from SWx_Dailly_View_Project.kp_forecast.utils import formatted_data_fetch


class GetTodayKpService:

    @staticmethod
    def kp_rate_today():
        file_date, formatted_data = formatted_data_fetch()
        kp_rates_output = [data['kp'] for data in formatted_data if data['time_tag'].split(" ", 1)[0] == file_date]
        kp_rate_dict = dict(Counter(kp_rates_output))
        response = {'kp_index': max(kp_rate_dict, key=kp_rate_dict.get)}
        kp_index = int(response['kp_index'])
        if kp_index >= 5:
            if kp_index == 5:
                response['noaa_scale'] = 'G1'
            elif kp_index == 6:
                response['noaa_scale'] = 'G2'
            elif kp_index == 7:
                response['noaa_scale'] = 'G3'
            elif kp_index == 8:
                response['noaa_scale'] = 'G4'
            elif kp_index == 9:
                response['noaa_scale'] = 'G5'
        else:
            response['noaa_scale'] = 'null'

        return response

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

        return [GetTodayKpService.time_interval_kp_rate(i) for i in formatted_data if
                i['time_tag'].split(" ", 1)[0] == file_date]

    @staticmethod
    def predicted_kp_index():

        file_date, formatted_data = formatted_data_fetch()

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

        return max(predicted_next_three_days_kp)
