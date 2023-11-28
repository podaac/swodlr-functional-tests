from requests import Response
from json import loads

from API.SWODLR import RasterDefinition

import config.globalvariables


globalVars = config.globalvariables.GlobalVariables

class TestRasterdefinition:
    def test_Rasterdefinition_GetRasterDefinitionsForCurrentUser_200(self):
        expectedStatusCode = 200
        response:Response = RasterDefinition.GetResterDefintionsOfCurrentUser(authorizationHeader = True)
        assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'


    def test_Rasterdefinition_GetRasterDefinitionsForCurrentUser_NoAuth_401(self): 
        expectedStatusCode = 401
        response:Response = RasterDefinition.GetResterDefintionsOfCurrentUser(authorizationHeader = False)
        assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'
    

    def test_Rasterdefinition_GetRasterDefinitionsForCurrentUser_InvalidAuth_401(self):
        expectedStatusCode = 401
        response:Response = RasterDefinition.GetResterDefintionsOfCurrentUser(authorizationHeader_invalid = True)
        assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'


    def test_Rasterdefinition_CreateAndDeleteRasterDefinition_200(self):
        rasterName = "test_Rasterdefinition_CreateAndDeleteRasterDefinition_200"
        expectedStatusCode = 200
        responseCreate:Response = RasterDefinition.CreateNewRasterDefinition(rasterName = rasterName, authorizationHeader = True)
        assert responseCreate.status_code == expectedStatusCode, f'Response code "{responseCreate.status_code}" is not "{expectedStatusCode}"!'
        jsonContent_Create = loads(responseCreate.text)
        rasterDefinitionId = jsonContent_Create['data']['createRasterDefinition']['id']
        assert rasterDefinitionId != "", f'Raster Definition ID is not returned! "{rasterDefinitionId}"!'

        response:Response = RasterDefinition.GetResterDefintionsOfCurrentUser(authorizationHeader = True)
        assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'
        jsonContent = loads(response.text)
        rasterDefinitions = jsonContent['data']['currentUser']['rasterDefinitions']
        found = False
        for raster in rasterDefinitions:
            if raster['id'] == rasterDefinitionId:
                found = True
        assert found, f'Previously created Raster Definition "{rasterDefinitionId}" is not among current user\'s raster definitions: "{rasterDefinitions}"'

        responseDelete:Response = RasterDefinition.DeleteRasterDefinition(rasterDefinitionId = rasterDefinitionId, authorizationHeader = True)
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
        responseCreate:Response = RasterDefinition.CreateNewRasterDefinition(rasterName = rasterName, authorizationHeader = True)
        assert responseCreate.status_code == expectedStatusCode, f'Response code "{responseCreate.status_code}" is not "{expectedStatusCode}"!'
        jsonContent_Create = loads(responseCreate.text)
        rasterDefinitionId = jsonContent_Create['data']['createRasterDefinition']['id']
        assert rasterDefinitionId != "", f'Raster Definition ID is not returned! "{rasterDefinitionId}"!'

        expectedStatusCode = 401
        response:Response = RasterDefinition.DeleteRasterDefinition(rasterDefinitionId = rasterDefinitionId, authorizationHeader_invalid = True)
        assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'

        expectedStatusCode = 200
        responseDelete:Response = RasterDefinition.DeleteRasterDefinition(rasterDefinitionId = rasterDefinitionId, authorizationHeader = True)
        assert responseDelete.status_code == expectedStatusCode, f'Response code "{responseDelete.status_code}" is not "{expectedStatusCode}"!' 
        jsonContent_Delete = loads(responseDelete.text)
        rasterDefinitionId = jsonContent_Delete['data']['deleteRasterDefinition']
        assert str(rasterDefinitionId).lower() == "true", f'Raster Definition: "{rasterDefinitionId}" is not deleted!'
