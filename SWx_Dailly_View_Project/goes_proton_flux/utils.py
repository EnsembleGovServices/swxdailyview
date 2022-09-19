from SWx_Dailly_View_Project.s3_services import fetch_bucket_data


def fetch_last_modified_proton_flux_file():
    bucket_data = fetch_bucket_data()
    lis = []
    for x in bucket_data.objects.filter(Prefix='proton flux/'):
        lis.append(x.last_modified)
    for x in bucket_data.objects.filter(Prefix='proton flux/'):
        if x.last_modified == lis[-1]:
            latest_file = x.key

    return latest_file
