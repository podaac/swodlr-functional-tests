from requests import Response
from json import loads
from random import choice
from string import ascii_lowercase, ascii_uppercase, digits

from API.SWODLR import RasterDefinition
from utils import Verifications

import config.globalvariables


globalVars = config.globalvariables.GlobalVariables

class TestRasterdefinition:

# ========================================== currentUser ==========================================

    def test_Rasterdefinition_GetRasterDefinitionsForCurrentUser_200(self):
        expectedStatusCode = 200
        response:Response = RasterDefinition.GetResterDefintionsOfCurrentUser()
        assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'


    def test_Rasterdefinition_GetRasterDefinitionsForCurrentUser_NoAuth_401(self): 
        expectedStatusCode = 401
        response:Response = RasterDefinition.GetResterDefintionsOfCurrentUser(authorizationHeader = False)
        assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'
    

    def test_Rasterdefinition_GetRasterDefinitionsForCurrentUser_InvalidAuth_401(self):
        expectedStatusCode = 401
        response:Response = RasterDefinition.GetResterDefintionsOfCurrentUser(authorizationHeader_invalid = True)
        assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'


# ========================================== createRasterDefinition ==========================================

    def test_Rasterdefinition_CreateAndDeleteRasterDefinition_200(self):
        rasterName = "test_Rasterdefinition_CreateAndDeleteRasterDefinition_200"
        expectedStatusCode = 200
        responseCreate:Response = RasterDefinition.CreateNewRasterDefinition(rasterName = rasterName)
        assert responseCreate.status_code == expectedStatusCode, f'Response code "{responseCreate.status_code}" is not "{expectedStatusCode}"!'
        jsonContent_Create = loads(responseCreate.text)
        rasterDefinitionId = jsonContent_Create['data']['createRasterDefinition']['id']
        globalVars.SWODLR_RasterDefinitionId = rasterDefinitionId
        assert rasterDefinitionId != "", f'Raster Definition ID is not returned! "{rasterDefinitionId}"!'

        response:Response = RasterDefinition.GetResterDefintionsOfCurrentUser()
        assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'
        jsonContent = loads(response.text)
        rasterDefinitions = jsonContent['data']['currentUser']['rasterDefinitions']
        found = False
        for raster in rasterDefinitions:
            if raster['id'] == rasterDefinitionId:
                found = True
        assert found, f'Previously created Raster Definition "{rasterDefinitionId}" is not among current user\'s raster definitions: "{rasterDefinitions}"'

        responseDelete:Response = RasterDefinition.DeleteRasterDefinition(rasterDefinitionId = rasterDefinitionId)
        assert responseDelete.status_code == expectedStatusCode, f'Response code "{responseDelete.status_code}" is not "{expectedStatusCode}"!' 
        jsonContent_Delete = loads(responseDelete.text)
        rasterDefinitionId = jsonContent_Delete['data']['deleteRasterDefinition']
        assert str(rasterDefinitionId).lower() == "true", f'Raster Definition: "{rasterDefinitionId}" is not deleted!'


    def test_Rasterdefinition_CreateRasterDefinition_NoAuth_401(self):
        rasterName = "test_Rasterdefinition_CreateRasterDefinition_NoAuth_401"
        expectedStatusCode = 401
        response:Response = RasterDefinition.CreateNewRasterDefinition(rasterName = rasterName, authorizationHeader = False)
        assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'


    def test_Rasterdefinition_CreateRasterDefinition_InvalidAuth_401(self):
        rasterName = "test_Rasterdefinition_CreateRasterDefinition_InvalidAuth_401"
        expectedStatusCode = 401
        response:Response = RasterDefinition.CreateNewRasterDefinition(rasterName = rasterName, authorizationHeader_invalid = True)
        assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'


    def test_Rasterdefinition_CreateRasterDefinition_Value_Empty_RasterName(self):
        response:Response = RasterDefinition.CreateNewRasterDefinition(rasterName = "")
        expectedStatusCode = 200
        expectedError = "length must be between 1 and 100"
        expectedType = "ValidationError"
        Verifications.ErrorVerification(
            response = response,
            fieldName = "",
            expectedStatusCode = expectedStatusCode,
            expectedError = expectedError,
            expectedType = expectedType
        )

    def test_Rasterdefinition_CreateRasterDefinition_Value_MaxLength_RasterName(self):
        randomString = ''.join(choice(ascii_uppercase + ascii_lowercase + digits) for _ in range(101))
        response:Response = RasterDefinition.CreateNewRasterDefinition(rasterName = randomString)
        expectedStatusCode = 200
        expectedError = "length must be between 1 and 100"
        expectedType = "ValidationError"
        Verifications.ErrorVerification(
            response = response,
            fieldName = "",
            expectedStatusCode = expectedStatusCode,
            expectedError = expectedError,
            expectedType = expectedType
        )

    
    def test_Rasterdefinition_CreateRasterDefinition_Type_Wrong_RasterName(self):
        response:Response = RasterDefinition.CreateNewRasterDefinition(rasterName = "test_Rasterdefinition_CreateRasterDefinition_Type_Wrong_RasterName", valueTypeError = {'rasterName':'integer'})
        expectedStatusCode = 200
        expectedError = "validation error of type wrongtype: argument 'name' with value 'enumvalue"
        expectedType = "ValidationError"
        Verifications.ErrorVerification(
            response = response,
            fieldName = "N/A",
            expectedStatusCode = expectedStatusCode,
            expectedError = expectedError,
            expectedType = expectedType,
            checkForData = False
        )


    def test_Rasterdefinition_CreateRasterDefinition_Type_Wrong_OutputGranuleExtentFlag(self):
        response:Response = RasterDefinition.CreateNewRasterDefinition(rasterName = "test_Rasterdefinition_CreateRasterDefinition_Type_Wrong_OutputGranuleExtentFlag",
            valueTypeError = {'outputGranuleExtentFlag':'string'})
        expectedStatusCode = 200
        expectedError = "validation error of type wrongtype: argument 'outputgranuleextentflag' with value 'stringvalue"
        expectedType = "ValidationError"
        Verifications.ErrorVerification(
            response = response,
            fieldName = "N/A",
            expectedStatusCode = expectedStatusCode,
            expectedError = expectedError,
            expectedType = expectedType,
            checkForData = False
        )

    
    def test_Rasterdefinition_CreateRasterDefinition_Type_Wrong_OutputSamplingGridType(self):
        response:Response = RasterDefinition.CreateNewRasterDefinition(rasterName = "test_Rasterdefinition_CreateRasterDefinition_Type_Wrong_OutputSamplingGridType",
            valueTypeError = {'outputSamplingGridType':'string'})
        expectedStatusCode = 200
        expectedError = "validation error of type wrongtype: argument 'outputsamplinggridtype' with value 'stringvalue"
        expectedType = "ValidationError"
        Verifications.ErrorVerification(
            response = response,
            fieldName = "N/A",
            expectedStatusCode = expectedStatusCode,
            expectedError = expectedError,
            expectedType = expectedType,
            checkForData = False
        )
    

    def test_Rasterdefinition_CreateRasterDefinition_Value_Wrong_RasterResolution_Negative(self):
        response:Response = RasterDefinition.CreateNewRasterDefinition(rasterName = "test_Rasterdefinition_CreateRasterDefinition_Value_Wrong_RasterResolution_Negative",
            rasterResolution =  -1)
        expectedStatusCode = 200
        expectedError = "must be a valid resolution according to the grid type"
        expectedType = "ValidationError"
        Verifications.ErrorVerification(
            response = response,
            fieldName = "N/A",
            expectedStatusCode = expectedStatusCode,
            expectedError = expectedError,
            expectedType = expectedType,
            checkForData = False
        )

    
    def test_Rasterdefinition_CreateRasterDefinition_Value_Wrong_RasterResolution_MaxLimit(self):
        response:Response = RasterDefinition.CreateNewRasterDefinition(rasterName = "test_Rasterdefinition_CreateRasterDefinition_Value_Wrong_RasterResolution_MaxLimit",
            rasterResolution = 10000000000)
        expectedStatusCode = 200
        expectedError = "validation error of type wrongtype: argument 'rasterresolution' with value 'intvalue{value=10000000000}' is not a valid 'int'"
        expectedType = "ValidationError"
        Verifications.ErrorVerification(
            response = response,
            fieldName = "N/A",
            expectedStatusCode = expectedStatusCode,
            expectedError = expectedError,
            expectedType = expectedType,
            checkForData = False
        )


    def test_Rasterdefinition_CreateRasterDefinition_Type_Wrong_RasterResolution_String(self):
        response:Response = RasterDefinition.CreateNewRasterDefinition(rasterName = "test_Rasterdefinition_CreateRasterDefinition_Type_Wrong_RasterResolution_String",
            valueTypeError = {'rasterResolution':'string'})
        expectedStatusCode = 200
        expectedError = "validation error of type wrongtype: argument 'rasterresolution' with value 'stringvalue"
        expectedType = "ValidationError"
        Verifications.ErrorVerification(
            response = response,
            fieldName = "N/A",
            expectedStatusCode = expectedStatusCode,
            expectedError = expectedError,
            expectedType = expectedType,
            checkForData = False
        )


    def test_Rasterdefinition_CreateRasterDefinition_Value_Wrong_UtmZoneAdjust_Negative(self):
        response:Response = RasterDefinition.CreateNewRasterDefinition(rasterName = "test_Rasterdefinition_CreateRasterDefinition_Value_Wrong_UtmZoneAdjust_Negative",
            utmZoneAdjust = -2)
        expectedStatusCode = 200
        expectedError = "must be one of: -1, 0, -1"
        expectedType = "ValidationError"
        Verifications.ErrorVerification(
            response = response,
            fieldName = "N/A",
            expectedStatusCode = expectedStatusCode,
            expectedError = expectedError,
            expectedType = expectedType,
            checkForData = False
        )


    def test_Rasterdefinition_CreateRasterDefinition_Value_Wrong_UtmZoneAdjust_MaxLimit(self):
        response:Response = RasterDefinition.CreateNewRasterDefinition(rasterName = "test_Rasterdefinition_CreateRasterDefinition_Value_Wrong_UtmZoneAdjust_MaxLimit",
            utmZoneAdjust = 10)
        expectedStatusCode = 200
        expectedError = "must be one of: -1, 0, -1"
        expectedType = "ValidationError"
        Verifications.ErrorVerification(
            response = response,
            fieldName = "N/A",
            expectedStatusCode = expectedStatusCode,
            expectedError = expectedError,
            expectedType = expectedType,
            checkForData = False
        )

    
    def test_Rasterdefinition_CreateRasterDefinition_Type_Wrong_UtmZoneAdjust(self):
        response:Response = RasterDefinition.CreateNewRasterDefinition(rasterName = "test_Rasterdefinition_CreateRasterDefinition_Type_Wrong_UtmZoneAdjust",
            valueTypeError = {'utmZoneAdjust':'string'})
        expectedStatusCode = 200
        expectedError = "validation error of type wrongtype: argument 'utmzoneadjust' with value 'stringvalue"
        expectedType = "ValidationError"
        Verifications.ErrorVerification(
            response = response,
            fieldName = "N/A",
            expectedStatusCode = expectedStatusCode,
            expectedError = expectedError,
            expectedType = expectedType,
            checkForData = False
        )


    def test_Rasterdefinition_CreateRasterDefinition_Value_Wrong_MgrsBandAdjust_Negative(self):
        response:Response = RasterDefinition.CreateNewRasterDefinition(rasterName = "test_Rasterdefinition_CreateRasterDefinition_Value_Wrong_MgrsBandAdjust_Negative",
            mgrsBandAdjust = -2)
        expectedStatusCode = 200
        expectedError = "must be one of: -1, 0, -1"
        expectedType = "ValidationError"
        Verifications.ErrorVerification(
            response = response,
            fieldName = "N/A",
            expectedStatusCode = expectedStatusCode,
            expectedError = expectedError,
            expectedType = expectedType,
            checkForData = False
        )


    def test_Rasterdefinition_CreateRasterDefinition_Value_Wrong_MgrsBandAdjust_MaxLimit(self):
        response:Response = RasterDefinition.CreateNewRasterDefinition(rasterName = "test_Rasterdefinition_CreateRasterDefinition_Value_Wrong_MgrsBandAdjust_MaxLimit",
            mgrsBandAdjust = 2)
        expectedStatusCode = 200
        expectedError = "must be one of: -1, 0, -1"
        expectedType = "ValidationError"
        Verifications.ErrorVerification(
            response = response,
            fieldName = "N/A",
            expectedStatusCode = expectedStatusCode,
            expectedError = expectedError,
            expectedType = expectedType,
            checkForData = False
        )

    
    def test_Rasterdefinition_CreateRasterDefinition_Type_Wrong_MgrsBandAdjust(self):
        response:Response = RasterDefinition.CreateNewRasterDefinition(rasterName = "test_Rasterdefinition_CreateRasterDefinition_Type_Wrong_MgrsBandAdjust",
            valueTypeError = {'mgrsBandAdjust':'string'})
        expectedStatusCode = 200
        expectedError = "validation error of type wrongtype: argument 'mgrsbandadjust' with value 'stringvalue"
        expectedType = "ValidationError"
        Verifications.ErrorVerification(
            response = response,
            fieldName = "N/A",
            expectedStatusCode = expectedStatusCode,
            expectedError = expectedError,
            expectedType = expectedType,
            checkForData = False
        )
    

# ========================================== deleteRasterDefinition ==========================================

    def test_Rasterdefinition_DeleteRasterDefinition_NoAuth_401(self):
        rasterName = "test_Rasterdefinition_DeleteRasterDefinition_NoAuth_401"
        expectedStatusCode = 200
        responseCreate:Response = RasterDefinition.CreateNewRasterDefinition(rasterName = rasterName, authorizationHeader = True)
        assert responseCreate.status_code == expectedStatusCode, f'Response code "{responseCreate.status_code}" is not "{expectedStatusCode}"!'
        jsonContent_Create = loads(responseCreate.text)
        rasterDefinitionId = jsonContent_Create['data']['createRasterDefinition']['id']
        assert rasterDefinitionId != "", f'Raster Definition ID is not returned! "{rasterDefinitionId}"!'

        expectedStatusCode = 401
        response:Response = RasterDefinition.DeleteRasterDefinition(rasterDefinitionId = rasterDefinitionId, authorizationHeader = False)
        assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'

        expectedStatusCode = 200
        responseDelete:Response = RasterDefinition.DeleteRasterDefinition(rasterDefinitionId = rasterDefinitionId, authorizationHeader = True)
        assert responseDelete.status_code == expectedStatusCode, f'Response code "{responseDelete.status_code}" is not "{expectedStatusCode}"!' 
        jsonContent_Delete = loads(responseDelete.text)
        rasterDefinitionId = jsonContent_Delete['data']['deleteRasterDefinition']
        assert str(rasterDefinitionId).lower() == "true", f'Raster Definition: "{rasterDefinitionId}" is not deleted!'


    def test_Rasterdefinition_DeleteRasterDefinition_InvalidAuth_401(self):
        rasterName = "test_Rasterdefinition_DeleteRasterDefinition_InvalidAuth_401"
        expectedStatusCode = 200
        responseCreate:Response = RasterDefinition.CreateNewRasterDefinition(rasterName = rasterName)
        assert responseCreate.status_code == expectedStatusCode, f'Response code "{responseCreate.status_code}" is not "{expectedStatusCode}"!'
        jsonContent_Create = loads(responseCreate.text)
        rasterDefinitionId = jsonContent_Create['data']['createRasterDefinition']['id']
        assert rasterDefinitionId != "", f'Raster Definition ID is not returned! "{rasterDefinitionId}"!'

        expectedStatusCode = 401
        response:Response = RasterDefinition.DeleteRasterDefinition(rasterDefinitionId = rasterDefinitionId, authorizationHeader_invalid = True)
        assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'

        expectedStatusCode = 200
        responseDelete:Response = RasterDefinition.DeleteRasterDefinition(rasterDefinitionId = rasterDefinitionId)
        assert responseDelete.status_code == expectedStatusCode, f'Response code "{responseDelete.status_code}" is not "{expectedStatusCode}"!' 
        jsonContent_Delete = loads(responseDelete.text)
        rasterDefinitionId = jsonContent_Delete['data']['deleteRasterDefinition']
        assert str(rasterDefinitionId).lower() == "true", f'Raster Definition: "{rasterDefinitionId}" is not deleted!'


    def test_Rasterdefinition_DeleteRasterDefinition_Value_Empty_RasterDefinitionID(self):
        response:Response = RasterDefinition.DeleteRasterDefinition(rasterDefinitionId = "")
        expectedStatusCode = 200
        expectedError = "raster definition not found"
        expectedType = "DataFetchingException"
        Verifications.ErrorVerification(
            response = response,
            fieldName = "",
            expectedStatusCode = expectedStatusCode,
            expectedError = expectedError,
            expectedType = expectedType
        )

    def test_Rasterdefinition_DeleteRasterDefinition_Value_Wrong_ProductID(self):
        response:Response = RasterDefinition.DeleteRasterDefinition(rasterDefinitionId = globalVars.SWODLR_RasterDefinitionId)
        expectedStatusCode = 200
        expectedError = "raster definition not found"
        expectedType = "DataFetchingException"
        Verifications.ErrorVerification(
            response = response,
            fieldName = "",
            expectedStatusCode = expectedStatusCode,
            expectedError = expectedError,
            expectedType = expectedType
        )

    
    def test_Rasterdefinition_DeleteRasterDefinition_Type_Wrong_RasterDefinitionID(self):
        response:Response = RasterDefinition.DeleteRasterDefinition(rasterDefinitionId = globalVars.SWODLR_RasterDefinitionId, valueTypeError = {'id':'integer'})
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
