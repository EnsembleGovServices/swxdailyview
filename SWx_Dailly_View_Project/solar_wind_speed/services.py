from datetime import datetime, timedelta
from flask import request

from SWx_Dailly_View_Project.s3_services import get_s3_client, BUCKET_NAME


class GetSolarWindSpeedService:

    @staticmethod
    def get_solar_wind_speed():
        """
            Returns solar wind speed
        """
        if request.args.get('time_stamp'):
            time_stamp = int(request.args.get('time_stamp'))
        else:
            time_stamp = datetime.now().timestamp()

        datetime_obj = datetime.fromtimestamp(time_stamp)
        past_date_obj = datetime_obj - timedelta(days=1)
        # date = str(datetime_obj.date()).replace('-', '.')
        time_range = str(datetime_obj).split()[1].split(":")[0] + str(datetime_obj).split()[1].split(":")[1]
        req_date = (str(datetime_obj).split()[0]).replace("-", ".")
        req_past = (str(past_date_obj).split()[0]).replace("-", ".")

        # THIS IS FOR REFERENCE
        # print(f"This is date: {datetime_obj} and this is time: {time_range}"
        #       f"This is req_date: {req_date}"
        #       f"This is req_date: {req_past}")

        time = time_range[:2]
        time_files = []
        req_date_lis = []
        if time == "00":
            time_files.extend(["1615", "1630", "1645", "1700"])
            req_date_lis.append(req_date)

        elif time == "01":
            time_files.extend([1715, 1730, 1745, 1800])
            req_date_lis.append(req_past)

        elif time == "02":
            time_files.extend([1815, 1830, 1845, 1900])
            req_date_lis.append(req_past)

        elif time == "03":
            time_files.extend([1915, 1930, 1945, 2000])
            req_date_lis.append(req_past)

        elif time == "04":
            time_files.extend([2015, 2030, 2045, 2100])
            req_date_lis.append(req_past)

        elif time == "05":
            time_files.extend([2115, 2130, 2145, 2200])
            req_date_lis.append(req_past)

        elif time == "06":
            time_files.extend([2215, 2230, 2245, 2300])
            req_date_lis.append(req_past)

        elif time == "07":
            time_files.extend([2315, 2330, 2345, 0000])
            req_date_lis.append(req_past)

        elif time == "08":
            time_files.extend(["0015", "0030", "0045", "0100"])
            req_date_lis.append(req_date)

        elif time == "09":
            time_files.extend(["0115", "0130", "0145", "0200"])
            req_date_lis.append(req_date)

        elif time == "10":
            time_files.extend(["0215", "0230", "0245", "0300"])
            req_date_lis.append(req_date)

        elif time == "11":
            time_files.extend(["0315", "0330", "0345", "0400"])
            req_date_lis.append(req_date)

        elif time == "12":
            time_files.extend(["0415", "0430", "0445", "0500"])
            req_date_lis.append(req_date)

        elif time == "13":
            time_files.extend(["0515", "0530", "0545", "0600"])
            req_date_lis.append(req_date)

        elif time == "14":
            time_files.extend(["0615", "0630", "0645", "0700"])
            req_date_lis.append(req_date)

        elif time == "15":
            time_files.extend(["0715", "0730", "0745", "0800"])
            req_date_lis.append(req_date)

        elif time == "16":
            time_files.extend(["0815", "0830", "0845", "0900"])
            req_date_lis.append(req_date)

        elif time == "17":
            time_files.extend(["0915", "0930", "0945", "1000"])
            req_date_lis.append(req_date)

        elif time == "18":
            time_files.extend(["1015", "1030", "1045", "1100"])
            req_date_lis.append(req_date)

        elif time == "19":
            time_files.extend(["1115", "1130", "1145", "1200"])
            req_date_lis.append(req_date)

        elif time == "20":
            time_files.extend(["1215", "1230", "1245", "1300"])
            req_date_lis.append(req_date)

        elif time == "21":
            time_files.extend(["1315", "1330", "1345", "1400"])
            req_date_lis.append(req_date)

        elif time == "22":
            time_files.extend(["1415", "1430", "1445", "1500"])
            req_date_lis.append(req_date)

        elif time == "23":
            time_files.extend(["1515", "1530", "1545", "1600"])
            req_date_lis.append(req_date)

        files = [f"solar wind/Solar Wind {req_date_lis[0]} {inter}.json" for inter in time_files]

        # THIS ALL FILES GOING TO FETCH FROM S3 buckets.
        # print("this is files: ", files)

        ans = 0
        count = 0
        for file in files:

            s3_client = get_s3_client()
            try:
                response = s3_client.get_object(Bucket=BUCKET_NAME, Key=file)
                raw_data = response.get('Body')
                data = raw_data.read().decode('UTF-8')
                data = eval(f"{data}")
                for value in data:
                    ans += value['bt']
                    count += 1
            except:
                pass
        return_res = {"avg_bt":ans/count} if count != 0 else {"avg_bt":0}
        return return_res