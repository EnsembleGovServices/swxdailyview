from collections import Counter
from http import HTTPStatus

from SWx_Dailly_View_Project.constants import FILE_NOT_FETCHED, ISSUE_IN_FETCHING_DATA
from SWx_Dailly_View_Project.languages import Response
from SWx_Dailly_View_Project.latitude_index.utils import fetch_last_modified_mid_latitude_file, \
    fetch_last_modified_high_latitude_file, get_g_percentage, get_csv_data


class GetMidLatitudeResource:

    @staticmethod
    def get_mid_latitude():
        # g_dict = {5: 'G1', 6: 'G2', 7: 'G3', 8: 'G4', 9: 'G5'}
        if not fetch_last_modified_mid_latitude_file():
            return Response(status_code=HTTPStatus.BAD_REQUEST,
                            message=FILE_NOT_FETCHED).send_error_response()
        file_name = fetch_last_modified_mid_latitude_file()
        csv_data = get_csv_data(file_name)
        predicted_days_kp = [csv_data.iloc[i][2] for i in range(len(csv_data))] + [csv_data.iloc[i][3] for i in
                                                                                   range(len(csv_data))]
        if not get_g_percentage(Counter(predicted_days_kp)):
            return Response(status_code=HTTPStatus.BAD_REQUEST,
                            message=ISSUE_IN_FETCHING_DATA).send_error_response()

        return get_g_percentage(Counter(predicted_days_kp))


class GetHighLatitudeResource:

    @staticmethod
    def get_high_latitude():
        if not fetch_last_modified_high_latitude_file():
            return Response(status_code=HTTPStatus.BAD_REQUEST,
                            message=FILE_NOT_FETCHED).send_error_response()
        file_name = fetch_last_modified_high_latitude_file()
        csv_data = get_csv_data(file_name)
        predicted_days_kp = [csv_data.iloc[i][2] for i in range(len(csv_data))] + [csv_data.iloc[i][3] for i in
                                                                                   range(len(csv_data))]
        if not get_g_percentage(Counter(predicted_days_kp)):
            return Response(status_code=HTTPStatus.BAD_REQUEST,
                            message=ISSUE_IN_FETCHING_DATA).send_error_response()

        return get_g_percentage(Counter(predicted_days_kp))