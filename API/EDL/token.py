import requests

import config.globalvariables


# File wide variables
HTTPBasicAuth = requests.models.HTTPBasicAuth
globalVars = config.globalvariables.GlobalVariables

class Token():

    def GetExistingToken():
        endpoint = "/api/users/tokens"
        url = globalVars.EDL_baseurl + endpoint
        response = requests.get(
            url = url,
            auth = HTTPBasicAuth(globalVars.EDL_Username, globalVars.EDL_Password))
        return response

    def RequestNewToken():
        endpoint = "/api/users/token"
        url = globalVars.EDL_baseurl + endpoint

        response = requests.post(
            url = url,
            auth = HTTPBasicAuth(globalVars.EDL_Username, globalVars.EDL_Password))
        return response

    def DeleteExistingToken(token:str):
        endpoint = "/api/users/revoke_token?token={0}".format(token)
        url = globalVars.EDL_baseurl + endpoint

        response = requests.post(
            url = url,
            auth = HTTPBasicAuth(globalVars.EDL_Username, globalVars.EDL_Password))
        return response
