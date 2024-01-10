from requests import Response

from API.SWODLR import User

import config.globalvariables


globalVars = config.globalvariables.GlobalVariables

class TestUser:

# ========================================== currentUser ==========================================

    def test_User_GetCurrentUserDetails_Full_200(self):
        expectedStatusCode = 200
        response:Response = User.GetCurrentUserFullDetails(authorizationHeader = True)
        assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'


    def test_User_GetCurrentUserDetails_200(self):
        expectedStatusCode = 200
        response:Response = User.GetCurrentUser(authorizationHeader = True)
        assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'


    def test_User_GetCurrentUserDetails_NoAuth_401(self):
        expectedStatusCode = 401
        response:Response = User.GetCurrentUser(authorizationHeader = False)
        assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'
    

    def test_User_GetCurrentUserDetails_InvalidAuth_401(self):
        expectedStatusCode = 401
        response:Response = User.GetCurrentUser(authorizationHeader_invalid = True)
        assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'
