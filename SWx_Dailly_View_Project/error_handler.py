from http import HTTPStatus
from SWx_Dailly_View_Project.languages import Response
from flask import current_app


@current_app.errorhandler(404)
def page_not_found(error):
    return Response(status_code=HTTPStatus.NOT_FOUND).send_error_response()


@current_app.errorhandler(500)
def internal_server_error(error):
    return Response(status_code=HTTPStatus.NOT_FOUND).send_error_response()


@current_app.errorhandler(400)
def internal_server_error(error):
    return Response(status_code=HTTPStatus.BAD_REQUEST).send_error_response()


@current_app.errorhandler(204)
def no_content_error(error):
    return Response(status_code=HTTPStatus.NO_CONTENT).send_error_response()
