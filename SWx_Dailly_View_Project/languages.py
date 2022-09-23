from http import HTTPStatus

from flask import current_app as app


class Response:

    def __init__(self, status_code=HTTPStatus.OK, message=None, errors=None, data=None, ):
        self.status_code = status_code
        self.message = message
        self.data = data
        self.errors = errors

    def send_error_response(self):
        """
            send the Response for errors occurrence while fetching OUTPUT
        """
        response = self.errors or {'error': self.message or self.status_code.description}
        app.logger.error(response)
        return response, self.status_code


