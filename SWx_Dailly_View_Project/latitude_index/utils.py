from SWx_Dailly_View_Project.s3_services import fetch_bucket_data


def fetch_last_modified_mid_latitude_file():
    bucket_data = fetch_bucket_data()
    lis = []
    for x in bucket_data.objects.filter(Prefix='mid latitude k index/'):
        lis.append(x.last_modified)
    for x in bucket_data.objects.filter(Prefix='mid latitude k index/'):
        if x.last_modified == lis[-1]:
            latest_file = x.key
    print("this is latest: ",latest_file)

    return latest_file


def fetch_last_modified_high_latitude_file():
    bucket_data = fetch_bucket_data()
    lis = []
    for x in bucket_data.objects.filter(Prefix='high latitude k index/'):
        lis.append(x.last_modified)
    for x in bucket_data.objects.filter(Prefix='high latitude k index/'):
        if x.last_modified == lis[-1]:
            latest_file = x.key

    return latest_file
