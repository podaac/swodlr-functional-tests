import requests

import config.globalvariables


# File wide variables
globalVars = config.globalvariables.GlobalVariables

class GraphQlBase():
    
    def Base_Post(
            url:str,
            graphQlBody:str,
            authorizationHeader:bool = True,
            authorizationHeader_invalid:bool = False,
            logging:bool = True
            ) -> requests.Response:

        custom_header = {
            "Content-Type": "application/json" }
        if authorizationHeader:
            custom_header["Authorization"] = f"Bearer {globalVars.EDL_AccessToken}"
        if authorizationHeader_invalid:
            custom_header["Authorization"] = "Bearer asd"
    
        response = requests.post(
            url = url,
            headers = custom_header,
            json = {"query": graphQlBody})
        
        if logging:
            print(f"Response: {response.status_code}")
            print(f"Response text:\r\n{response.text}\r\n")
            print(f"Request url:\r\n{response.request.url}\r\n")
            print(f"Request body:\r\n{response.request.body}\r\n")
            # print(f"Token: {globalVars.EDL_AccessToken}")

        return response
    