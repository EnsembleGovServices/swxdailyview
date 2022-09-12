import json
from collections import Counter


class GetTodayKpService:

    @staticmethod
    def kp_rate_today():
        # right now we are using this static file
        f = open('converted_demo_kp_forecast_file.json')
        convert_data = json.load(f)
        f.close()
        kp_rates_output = []
        for i in convert_data:
            if i['time_tag'].split(" ", 1)[0] == '2022-08-28':
                kp_rates_output.append(i['kp'])
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
        f = open('converted_demo_kp_forecast_file.json')
        convert_data = json.load(f)
        f.close()

        kp_rate_as_per_intervals_list = []
        for i in convert_data:
            if i['time_tag'].split(" ", 1)[0] == '2022-08-28':
                kp_rate_as_per_intervals_list.append(GetTodayKpService.time_interval_kp_rate(i))

        return kp_rate_as_per_intervals_list

    @staticmethod
    def predicted_kp_index(desired_date):

        # for fetching data from the file we need to load that
        f = open('converted_demo_kp_forecast_file.json')
        convert_data = json.load(f)
        f.close()

        predicted_data = []
        for data in convert_data:
            if data['observed'] == 'predicted':
                predicted_data.append(data)

        from datetime import datetime
        date_time_str = desired_date
        date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')

        import datetime
        next_one_day = date_time_obj + datetime.timedelta(days=1)
        next_sec_day = date_time_obj + datetime.timedelta(days=2)
        next_third_day = date_time_obj + datetime.timedelta(days=3)

        next_three_dates = [str(next_one_day).split(" ", 1)[0],
                            str(next_sec_day).split(" ", 1)[0],
                            str(next_third_day).split(" ", 1)[0]]

        predicted_next_three_days_kp = []
        for observed_predicted_dates in predicted_data:
            if observed_predicted_dates['time_tag'].split(" ", 1)[0] in next_three_dates:
                predicted_next_three_days_kp.append(observed_predicted_dates['kp'])

        return max(predicted_next_three_days_kp)
