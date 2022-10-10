from datetime import datetime
from http import HTTPStatus

from flask import request

from SWx_Dailly_View_Project import cache
from SWx_Dailly_View_Project.constants import FILE_NOT_FETCHED, ISSUE_IN_FETCHING_DATA, HIGH_LATITUDE_FOLDER_NAME, \
    MID_LATITUDE_FOLDER_NAME
from SWx_Dailly_View_Project.languages import Response
from SWx_Dailly_View_Project.latitude_index.utils import get_g_percentage, fetch_latitude_file_name


class GetMidLatitudeResource:

    @staticmethod
    @cache.memoize(timeout=900)
    def get_mid_latitude():
        """
            Returns mid latitude data in percentage noaa_scale prediction probability
        """
        # g_dict = {5: 'G1', 6: 'G2', 7: 'G3', 8: 'G4', 9: 'G5'}

        if request.args.get('time_stamp'):
            time_stamp = int(request.args.get('time_stamp'))
        else:
            time_stamp = datetime.now().timestamp()
        if not fetch_latitude_file_name(time_stamp=time_stamp,
                                        folder_name=MID_LATITUDE_FOLDER_NAME):
            return Response(status_code=HTTPStatus.BAD_REQUEST,
                            message=FILE_NOT_FETCHED).send_error_response()
        file_name = fetch_latitude_file_name(time_stamp=time_stamp,
                                             folder_name=MID_LATITUDE_FOLDER_NAME)
        if not get_g_percentage(file_name):
            return Response(status_code=HTTPStatus.BAD_REQUEST,
                            message=ISSUE_IN_FETCHING_DATA).send_error_response()

        return get_g_percentage(file_name)


class GetHighLatitudeResource:

    @staticmethod
    @cache.memoize(timeout=900)
    def get_high_latitude():
        """
            Returns high latitude data in percentage noaa_scale prediction probability
        """
        if request.args.get('time_stamp'):
            time_stamp = int(request.args.get('time_stamp'))
        else:
            time_stamp = datetime.now().timestamp()
        if not fetch_latitude_file_name(time_stamp=time_stamp,
                                        folder_name=HIGH_LATITUDE_FOLDER_NAME):
            return Response(status_code=HTTPStatus.BAD_REQUEST,
                            message=FILE_NOT_FETCHED).send_error_response()
        file_name = fetch_latitude_file_name(time_stamp=time_stamp,
                                             folder_name=HIGH_LATITUDE_FOLDER_NAME)
        if not get_g_percentage(file_name):
            return Response(status_code=HTTPStatus.BAD_REQUEST,
                            message=ISSUE_IN_FETCHING_DATA).send_error_response()
        return get_g_percentage(file_name)
