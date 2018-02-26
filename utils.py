
from flask import Response

import json


def make_into_response(dic):
    return Response(json.dumps(dic), mimetype="text/json")


class ExceptionWithResponseDict(Exception):
    def get_resp_dict(self):
        assert (self.resp_dict is not None)

        return self.resp_dict
