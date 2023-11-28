from requests import Response
from json import loads

from API.SWODLR import Status

import config.globalvariables


globalVars = config.globalvariables.GlobalVariables

class TestStatus:
    def test_Status_GetStatusByProductId_200(self):
        expectedStatusCode = 200
        productId = globalVars.SWODLR_ProductId
        response:Response = Status.GetStatusByProductID(productId = productId, authorizationHeader = True)
        assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'
        jsonContent = loads(response.text)
        products = jsonContent['data']['statusByProduct']
        acceptedStates = ["new"]
        for product in products:
            stateId = product['id']
            state = product['state']
            assert str(state).lower() in acceptedStates, f'The Product\'s "{productId}" state "{stateId}" is "{state}", which is not among the accepted ones: "{acceptedStates}"!'

    
    def test_Status_GetStatusByProductId_NoAuth_401(self):
        expectedStatusCode = 401
        productId = globalVars.SWODLR_ProductId
        response:Response = Status.GetStatusByProductID(productId = productId, authorizationHeader = False)
        assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'


    def test_Status_GetStatusByProductId_InvalidAuth_401(self):
        expectedStatusCode = 401
        productId = globalVars.SWODLR_ProductId
        response:Response = Status.GetStatusByProductID(productId = productId, authorizationHeader_invalid = True)
        assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'
