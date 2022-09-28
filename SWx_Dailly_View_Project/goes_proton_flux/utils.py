from datetime import datetime

from flask import current_app

from SWx_Dailly_View_Project.constants import PROTON_FLUX_FOLDER_NAME, ERROR_DETECTED
from SWx_Dailly_View_Project.s3_services import fetch_bucket_data


class FetchFileUtil:

    @staticmethod
    def fetch_file_name(time_stamp):
        try:
            datetime_obj = datetime.fromtimestamp(time_stamp)
            date = str(datetime_obj.date()).replace('-', '.')
            time = str(datetime_obj).split()[1].split(":")[0] + str(datetime_obj).split()[1].split(":")[1]
            file_name = f"{date} {time}"
            bucket_data = fetch_bucket_data()
            files = [x.key for x in bucket_data.objects.filter(Prefix=PROTON_FLUX_FOLDER_NAME) if
                     str(x.key).split()[3] == file_name.split()[0] and str(x.key).split()[4].split(".")[0][:2] ==
                     file_name.split()[1][:2] and str(x.key).split()[4].split(".")[0] <= file_name.split()[1]]
            if files:
                return files[-1]
            else:
                try:
                    lis = [x.last_modified for x in bucket_data.objects.filter(Prefix=PROTON_FLUX_FOLDER_NAME)]

                    for x in bucket_data.objects.filter(Prefix=PROTON_FLUX_FOLDER_NAME):
                        if x.last_modified == lis[-1]:
                            return x.key
                except Exception as e:
                    current_app.logger.error(ERROR_DETECTED.format(e))
                    return None
        except Exception as e:
            current_app.logger.error(ERROR_DETECTED.format(e))
            return None
