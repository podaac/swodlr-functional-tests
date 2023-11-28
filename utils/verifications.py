from requests import Response
from json import loads


class Verifications:

    def ErrorVerification(response:Response, fieldName:str, expectedStatusCode:int, expectedError:str, expectedType:str, checkForData:bool=True):
        assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'
        jsonContent = loads(response.text)
        errors = jsonContent['errors']
        for error in errors:
            errorMessage = error['message']
            errorType = error['extensions']['classification']
            assert expectedError in errorMessage.lower(), f'The error message "{errorMessage}" does not contains "{expectedError}"!'
            assert errorType == expectedType, f'The error type is "{errorType}" instead of "{expectedType}"!'
        if checkForData:
            if fieldName == "":
                resultList = jsonContent['data']
            else:
                resultList = jsonContent['data'][fieldName]
            assert resultList == None, f'Result is not None! Instead it is: "{resultList}"'