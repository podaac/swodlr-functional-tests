import requests

import config.globalvariables


# File wide variables
HTTPBasicAuth = requests.models.HTTPBasicAuth
globVar = config.globalvariables.GlobalVariables

class Token():

    def GetExistingToken():
        endpoint = "/api/users/tokens"
        url = globVar.EDL_baseurl + endpoint
        response = requests.get(
            url = url,
            auth = HTTPBasicAuth(globVar.EDL_Username, globVar.EDL_Password))
        return response

    def RequestNewToken():
        endpoint = "/api/users/token"
        url = globVar.EDL_baseurl + endpoint

        response = requests.post(
            url = url,
            auth = HTTPBasicAuth(globVar.EDL_Username, globVar.EDL_Password))
        return response

    def DeleteExistingToken(token:str):
        endpoint = "/api/users/revoke_token?token={0}".format(token)
        url = globVar.EDL_baseurl + endpoint

        response = requests.post(
            url = url,
            auth = HTTPBasicAuth(globVar.EDL_Username, globVar.EDL_Password))
        return response
