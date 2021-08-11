from .json_util import is_valid_json


class ResponseBuilder:
    def __init__(self):
        self.__response = {"message": None, "data": None, "status": None, "errors": None}

    @property
    def errors(self):
        return self.__response['errors']

    @errors.setter
    def errors(self, value):
        self.__response['errors'] = value

    @property
    def message(self):
        return self.__response['message']

    @message.setter
    def message(self, value):
        self.__response['message'] = value

    @property
    def data(self):
        return self.__response['data']

    @data.setter
    def data(self, value):
        self.__response['data'] = value

    @property
    def status(self):
        return self.__response['status']

    @status.setter
    def status(self, value):
        if isinstance(value, bool):
            self.__response['status'] = value
        else:
            raise ValueError('invalid value')

    def to_dict(self):
        response = self.__response
        if is_valid_json(response):
            return response
        else:
            raise TypeError("make sure all value is json valid. str, int, bool, list, dict")
