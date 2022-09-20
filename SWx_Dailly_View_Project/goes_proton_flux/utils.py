from SWx_Dailly_View_Project.constants import PROTON_FLUX_FOLDER_NAME
from SWx_Dailly_View_Project.s3_services import fetch_bucket_data


def fetch_last_modified_proton_flux_file():
    bucket_data = fetch_bucket_data()
    lis = [x.last_modified for x in bucket_data.objects.filter(Prefix=PROTON_FLUX_FOLDER_NAME)]
    for x in bucket_data.objects.filter(Prefix=PROTON_FLUX_FOLDER_NAME):
        if x.last_modified == lis[-1]:
            latest_file = x.key
    return latest_file
