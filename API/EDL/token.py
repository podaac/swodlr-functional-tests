import requests

import config


# File wide variables
HTTPBasicAuth = requests.models.HTTPBasicAuth
conf = config.config.Config

class Token():

    def GetExistingToken():
        endpoint = "/api/users/tokens"
        url = conf.EDL_baseurl + endpoint

        response = requests.get(
            url = url,
            auth = HTTPBasicAuth(conf.EDL_Username, conf.EDL_Password))
        return response

    def RequestNewToken():
        endpoint = "/api/users/token"
        url = conf.EDL_baseurl + endpoint

        response = requests.post(
            url = url,
            auth = HTTPBasicAuth(conf.EDL_Username, conf.EDL_Password))
        return response

    def DeleteExistingToken(token:str):
        endpoint = "/api/users/revoke_token?token={0}".format(token)
        url = conf.EDL_baseurl + endpoint

        response = requests.post(
            url = url,
            auth = HTTPBasicAuth(conf.EDL_Username, conf.EDL_Password))
        return response
