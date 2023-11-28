from requests import Response
from json import loads

from API.SWODLR import Status
from utils import Verifications

import config.globalvariables


globalVars = config.globalvariables.GlobalVariables
acceptedStates = ['new', 'available', 'ready']

class TestStatus:

# ========================================== statusByProduct ==========================================

    def test_Status_GetStatusByProductId_200(self):
        expectedStatusCode = 200
        productId = globalVars.SWODLR_ProductId
        response:Response = Status.GetStatusByProductID(productId = productId)
        assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'
        jsonContent = loads(response.text)
        statuses = jsonContent['data']['statusByProduct']
        for status in statuses:
            stateId = status['id']
            globalVars.SWODLR_StateId = stateId
            state = status['state']
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


    def test_Status_GetStatusByProductId_Value_Empty_ProductID(self):
        response:Response = Status.GetStatusByProductID(productId = "")
        expectedStatusCode = 200
        expectedError = 'internal_error'
        expectedType = "INTERNAL_ERROR"
        fieldName = 'statusByProduct'
        Verifications.ErrorVerification(
            response = response,
            fieldName = fieldName,
            expectedStatusCode = expectedStatusCode,
            expectedError = expectedError,
            expectedType = expectedType
        )


    def test_Status_GetStatusByProductId_Value_Wrong_ProductID(self):
        response:Response = Status.GetStatusByProductID(productId = globalVars.SWODLR_StateId)
        expectedStatusCode = 200
        expectedError = "invalid `product` parameter"
        expectedType = "DataFetchingException"
        fieldName = 'statusByProduct'
        Verifications.ErrorVerification(
            response = response,
            fieldName = fieldName,
            expectedStatusCode = expectedStatusCode,
            expectedError = expectedError,
            expectedType = expectedType
        )

    
    def test_Status_GetStatusByProductId_Type_Wrong_ProductID(self):
        response:Response = Status.GetStatusByProductID(productId = globalVars.SWODLR_ProductId, valueTypeError = {'productId':'integer'})
        expectedStatusCode = 200
        expectedError = "invalid syntax : "
        expectedType = "InvalidSyntax"
        Verifications.ErrorVerification(
            response = response,
            fieldName = "N/A",
            expectedStatusCode = expectedStatusCode,
            expectedError = expectedError,
            expectedType = expectedType,
            checkForData = False
        )


    def test_Status_GetStatusByProductId_Type_Wrong_Limit(self):
        response:Response = Status.GetStatusByProductID(productId = globalVars.SWODLR_ProductId, valueTypeError = {'limit':'string'})
        expectedStatusCode = 200
        expectedError = "validation error of type wrongtype: argument 'limit' with value 'stringvalue"
        expectedType = "ValidationError"
        Verifications.ErrorVerification(
            response = response,
            fieldName = "N/A",
            expectedStatusCode = expectedStatusCode,
            expectedError = expectedError,
            expectedType = expectedType,
            checkForData = False
        )
    

# ========================================== statusByPrevious ==========================================

    def test_Status_GetStatusByPrevious_200(self):
        expectedStatusCode = 200
        stateId = globalVars.SWODLR_StateId
        response:Response = Status.GetStatusByPrevious(statusId = stateId)
        assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'
        jsonContent = loads(response.text)
        statuses = jsonContent['data']['statusByPrevious']
        if len(statuses) == 0:
            assert True, 'No other statuses are present!'
        for status in statuses:
            stateId = status['id']
            state = status['state']
            assert str(state).lower() in acceptedStates, f'The Status "{stateId}" is "{state}", which is not among the accepted ones: "{acceptedStates}"!'


    def test_Status_GetStatusByPrevious_NoAuth_401(self):
        expectedStatusCode = 401
        response:Response = Status.GetStatusByPrevious(statusId = globalVars.SWODLR_StateId, authorizationHeader = False)
        assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'


    def test_Status_GetStatusByPrevious_InvalidAuth_401(self):
        expectedStatusCode = 401
        response:Response = Status.GetStatusByPrevious(statusId = globalVars.SWODLR_StateId, authorizationHeader_invalid = True)
        assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'


    def test_Status_GetStatusByPrevious_Value_Empty_StatusID(self):
        response:Response = Status.GetStatusByPrevious(statusId = "")
        expectedStatusCode = 200
        expectedError = 'internal_error'
        expectedType = "INTERNAL_ERROR"
        fieldName = 'statusByPrevious'
        Verifications.ErrorVerification(
            response = response,
            fieldName = fieldName,
            expectedStatusCode = expectedStatusCode,
            expectedError = expectedError,
            expectedType = expectedType
        )
    

    def test_Status_GetStatusByPrevious_Value_Wrong_StatusID(self):
        response:Response = Status.GetStatusByPrevious(statusId = globalVars.SWODLR_ProductId)
        expectedStatusCode = 200
        expectedError = "invalid `after` parameter"
        expectedType = "DataFetchingException"
        fieldName = 'statusByPrevious'
        Verifications.ErrorVerification(
            response = response,
            fieldName = fieldName,
            expectedStatusCode = expectedStatusCode,
            expectedError = expectedError,
            expectedType = expectedType
        )


    def test_Status_GetStatusByPrevious_Type_Wrong_StatusID(self):
        response:Response = Status.GetStatusByPrevious(statusId = globalVars.SWODLR_StateId, valueTypeError = {'statusId':'integer'})
        expectedStatusCode = 200
        expectedError = "invalid syntax : "
        expectedType = "InvalidSyntax"
        Verifications.ErrorVerification(
            response = response,
            fieldName = "N/A",
            expectedStatusCode = expectedStatusCode,
            expectedError = expectedError,
            expectedType = expectedType,
            checkForData = False
        )


    def test_Status_GetStatusByPrevious_Type_Wrong_Limit(self):
        response:Response = Status.GetStatusByPrevious(statusId = globalVars.SWODLR_StateId, valueTypeError = {'limit':'string'})
        expectedStatusCode = 200
        expectedError = "validation error of type wrongtype: argument 'limit' with value 'stringvalue"
        expectedType = "ValidationError"
        Verifications.ErrorVerification(
            response = response,
            fieldName = "N/A",
            expectedStatusCode = expectedStatusCode,
            expectedError = expectedError,
            expectedType = expectedType,
            checkForData = False
        )
