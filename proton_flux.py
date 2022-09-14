import json
import os
from io import StringIO

import boto3
from dotenv import load_dotenv

load_dotenv()

ACCESS_KEY = os.getenv("ACCESS_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
BUCKET_NAME = os.getenv("BUCKET_NAME")

s3_client = boto3.client("s3", aws_access_key_id=ACCESS_KEY,
                         aws_secret_access_key=SECRET_KEY)

import pandas as pd

file_name = 'proton flux/Proton Flux 2022.09.08 1702.csv'
response = s3_client.get_object(Bucket=BUCKET_NAME, Key=file_name)
raw_data = response.get('Body')
data = raw_data.read().decode('UTF-8')

csv_data = pd.read_csv(StringIO(data))
# print(">>",len(csv_data))

# energy = csv_data.iloc[2]['energy']
# print("this is energy: ",energy)
# print("this is value in energy:",energy.split()[0].split("=")[1])

proton_flux = {
    # "gt_1": [],
    "gt_10": [],
    "gt_50": [],
    "gt_100": [],
    # "gt_500": []
}


def append_in_proton_flux(dic_key, row_data):
    proton_flux[dic_key].append(
        {"time_tag": csv_data.iloc[row_data]['time_tag'],
         "flux": csv_data.iloc[row_data]['flux']
         }
    )


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

# 
# filehandler = open('proton', 'wt')
# data = str(proton_flux)
# filehandler.write(data)

# for save the dic data into json file [ we already saved it doesn't need to save again ]
# with open("proton.json", "w") as write_file:
#     json.dump(proton_flux, write_file, indent=4)
