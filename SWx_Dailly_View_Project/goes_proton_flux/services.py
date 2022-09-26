from datetime import timedelta, datetime
from http import HTTPStatus

import pandas as pd
from io import StringIO

from SWx_Dailly_View_Project.constants import FILE_NOT_FETCHED, REQUESTED_PARA_IS_INVALID_ARGS, \
    INVALID_INTERVAL_FOR_HOURS, INVALID_INTERVAL_FOR_DAYS
from SWx_Dailly_View_Project.goes_proton_flux.utils import FetchFileUtil
from SWx_Dailly_View_Project.languages import Response
from SWx_Dailly_View_Project.s3_services import get_s3_client, BUCKET_NAME


class GetProtonFluxService:

    @staticmethod
    def proton_flux_data(request):
        """
            Returns the response in dictionary format
            for particular requested time period such as here we have
            [ 6 Hours, 1 day, 3 days, 7 days ]
            :params: file_name which has the last modified file from the s3 buckets
            csv_data: is the pandas dataframe converted csv file into dataframe
            will get data in 3 parts [ gt_10,gt_50,gt_100 ] respectively.
        """

        s3_client = get_s3_client()
        valid_args = ['hours', 'days']
        valid_args_value = [1, 3, 7]
        keys = request.args.to_dict().keys()
        for i in keys:
            if i not in valid_args:
                return Response(status_code=HTTPStatus.BAD_REQUEST,
                                message=REQUESTED_PARA_IS_INVALID_ARGS).send_error_response()
        if request.args.get('hours') and int(request.args.get('hours')) != 6:
            return Response(status_code=HTTPStatus.BAD_REQUEST,
                            message=INVALID_INTERVAL_FOR_HOURS).send_error_response()
        if request.args.get('days') and int(request.args.get('days')) not in valid_args_value:
            return Response(status_code=HTTPStatus.BAD_REQUEST,
                            message=INVALID_INTERVAL_FOR_DAYS).send_error_response()

        # fetch particular file from the bucket
        # file_name = 'proton flux/Proton Flux 2022.09.15 1200.csv' [ for sample file name ]
        fetch_file_obj = FetchFileUtil()
        if not fetch_file_obj.fetch_last_modified_proton_flux_file():
            return Response(status_code=HTTPStatus.BAD_REQUEST,
                            message=FILE_NOT_FETCHED).send_error_response()
        file_name = fetch_file_obj.fetch_last_modified_proton_flux_file()
        response = s3_client.get_object(Bucket=BUCKET_NAME, Key=file_name)
        raw_data = response.get('Body')
        data = raw_data.read().decode('UTF-8')

        file_date = file_name.split()[3]
        date_time_str = file_date + ' 00:00:00'
        date_time_str = date_time_str.replace(".", "-")
        date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
        date_obj = str(date_time_obj).split()
        date_list = date_obj[0].split("-")
        desired_date_list = [date_list[1], date_list[2], date_list[0]]
        desired_date = ""

        for i in range(len(desired_date_list)):
            if i != 0:
                desired_date += "/"
            desired_date += desired_date_list[i]

        csv_data = pd.read_csv(StringIO(data))
        if request.args.get('days') == "1":
            drop_lis = [i for i in range(len(csv_data)) if csv_data.iloc[i]['time_tag'].split()[0] != desired_date]

            csv_data.drop(drop_lis, axis=0, inplace=True)

        # for 3 days request
        if request.args.get('days') == '3':
            desired_three_dates = [desired_date]
            date_time_str = desired_date + ' 00:00:00'

            current_date_formate = datetime.strptime(date_time_str, '%m/%d/%Y %H:%M:%S')

            last_one_day = current_date_formate - timedelta(days=1)
            last_sec_day = current_date_formate - timedelta(days=2)

            last_two_days = [str(last_one_day).split(" ", 1)[0].replace("-", "/"),
                             str(last_sec_day).split(" ", 1)[0].replace("-", "/")]

            for date in last_two_days:
                lis = date.split("/")
                new_date = [lis[1], lis[2], lis[0]]
                format_date = ""
                for i in range(len(new_date)):
                    if i != 0:
                        format_date += "/"
                    format_date += new_date[i]
                desired_three_dates.append(format_date)

            drop_lis = [i for i in range(len(csv_data)) if
                        csv_data.iloc[i]['time_tag'].split()[0] not in desired_three_dates]

            csv_data.drop(drop_lis, axis=0, inplace=True)

        if request.args.get("hours") == "6":
            str_date = desired_date + " 15:00:00"
            current_date = datetime.strptime(str_date, '%m/%d/%Y %H:%M:%S')
            desired_time_lis = [str(current_date)[:13]]
            for _ in range(5):
                current_date = current_date - timedelta(hours=1)
                desired_time_lis.append(str(current_date)[:13])

            for index, item in enumerate(desired_time_lis):
                desired_time_lis[index] = item.replace('-', '/')

            drop_lis = [i for i in range(len(csv_data)) if
                        (str(datetime.strptime(str(csv_data.iloc[i]['time_tag'][:13]), '%m/%d/%Y %H'))[:13]).replace(
                            '-', '/') not in desired_time_lis]

            csv_data.drop(drop_lis, axis=0, inplace=True)

        proton_flux = {
            "gt_10": [],
            "gt_50": [],
            "gt_100": [],
        }

        for i in range(len(csv_data)):

            if 10 <= int(csv_data.iloc[i]['energy'].split()[0].split("=")[1]) < 50:
                proton_flux['gt_10'].append(
                    {"time_tag": csv_data.iloc[i]['time_tag'],
                     "flux": csv_data.iloc[i]['flux']
                     }
                )
            elif 50 <= int(csv_data.iloc[i]['energy'].split()[0].split("=")[1]) < 100:
                proton_flux['gt_50'].append(
                    {"time_tag": csv_data.iloc[i]['time_tag'],
                     "flux": csv_data.iloc[i]['flux']
                     }
                )

            elif int(csv_data.iloc[i]['energy'].split()[0].split("=")[1]) >= 100:
                proton_flux['gt_100'].append(
                    {"time_tag": csv_data.iloc[i]['time_tag'],
                     "flux": csv_data.iloc[i]['flux']
                     }

                )

        return proton_flux
