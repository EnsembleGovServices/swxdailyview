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
    def proton_flux_data(duration):

        s3_client = boto3.client(
            "s3",
            aws_access_key_id=ACCESS_KEY,
            aws_secret_access_key=SECRET_KEY)

        file_name = 'proton flux/Proton Flux 2022.09.08 1702.csv'
        response = s3_client.get_object(Bucket=BUCKET_NAME, Key=file_name)
        raw_data = response.get('Body')
        data = raw_data.read().decode('UTF-8')
        # file_date = file_name.split()[3]
        # file_name.replace(".", "-")
        # from datetime import datetime
        # date_time_str = file_date + ' 00:00:00'
        # date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
        # formatted_data = utils.convert_into_json(file_name=file_name)

        # print("this is date: ",date_time_obj)

        csv_data = pd.read_csv(StringIO(data))
        # print(csv_data)
        print("------------------")

        if duration == '6 Hours':
            pass


        # print(duration)


        proton_flux = {
            # "gt_1": [],
            "gt_10": [],
            "gt_50": [],
            "gt_100": [],
            # "gt_500": []
        }

        for i in range(len(csv_data)):

            # if int(csv_data.iloc[i]['energy'].split()[0].split("=")[1]) <= 9:
            #     append_in_proton_flux(dic_key='gt_1',row_data=i)
            #     # proton_flux['gt_1'].append(
            #     #     {"time_tag": csv_data.iloc[i]['time_tag'],
            #     #      "flux": csv_data.iloc[i]['flux']
            #     #      }
            #     # )
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
            # elif 100 <= int(csv_data.iloc[i]['energy'].split()[0].split("=")[1]) < 500:
            #     proton_flux['gt_100'].append(
            #         {"time_tag": csv_data.iloc[i]['time_tag'],
            #          "flux": csv_data.iloc[i]['flux']
            #          }
            #     )
            elif int(csv_data.iloc[i]['energy'].split()[0].split("=")[1]) >= 100:
                proton_flux['gt_100'].append(
                    {"time_tag": csv_data.iloc[i]['time_tag'],
                     "flux": csv_data.iloc[i]['flux']
                     }

                )

        return proton_flux