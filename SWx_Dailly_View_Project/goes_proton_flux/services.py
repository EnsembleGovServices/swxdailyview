import os
import pandas as pd
import boto3
from io import StringIO

from dotenv import load_dotenv

load_dotenv()

ACCESS_KEY = os.getenv("ACCESS_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
BUCKET_NAME = os.getenv("BUCKET_NAME")


class GetProtonFluxService:

    @staticmethod
    def proton_flux_data(args):

        # print("this is args: ",args.get("days"))

        s3_client = boto3.client(
            "s3",
            aws_access_key_id=ACCESS_KEY,
            aws_secret_access_key=SECRET_KEY)

        file_name = 'proton flux/Proton Flux 2022.09.08 2150.csv'
        response = s3_client.get_object(Bucket=BUCKET_NAME, Key=file_name)
        raw_data = response.get('Body')
        data = raw_data.read().decode('UTF-8')
        file_date = file_name.split()[3]
        from datetime import datetime
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

        # print("this is new date: ", desired_date)
        csv_data = pd.read_csv(StringIO(data))
        # duration = '1 Day'
        if args.get("days")==1:
            drop_lis = []
            for i in range(len(csv_data)):
                if csv_data.iloc[i]['time_tag'].split()[0] != desired_date:
                    drop_lis.append(i)
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
