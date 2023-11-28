from API.SWODLR.basecall import BaseCall

import requests
import json

import config.globalvariables


# File wide variables
globalVars = config.globalvariables.GlobalVariables
endpoint = "api/graphql"

class RasterDefinition():
    
    def GetResterDefintionsOfCurrentUser(
            authorizationHeader:bool = True,
            authorizationHeader_invalid:bool = False,
            logging:bool = True
            ) -> requests.Response:
        if logging:
            print(f'\r\nGetting Raster Definitions related to Current user...')

        graphQlBody = '''
            {
            	currentUser {
            		rasterDefinitions {
            			name
            			id
            			outputSamplingGridType
            			rasterResolution
            			outputGranuleExtentFlag
            			mgrsBandAdjust
            			utmZoneAdjust
            		}
            	}
            }
            '''
        
        response = BaseCall.Base_Post(
            url = f'{globalVars.SWODLR_baseurl}/{endpoint}',
            graphQlBody = graphQlBody,
            authorizationHeader = authorizationHeader,
            authorizationHeader_invalid = authorizationHeader_invalid,
            logging = logging
        )
        
        return response


    def CreateNewRasterDefinition(
            rasterName:str,
            authorizationHeader:bool = True,
            authorizationHeader_invalid:bool = False,
            logging:bool = True
            ) -> requests.Response:
        if logging:
            print(f'\r\nCreating a new Raster Definition related to Current user...')

        graphQlBody = '''
            mutation {
                createRasterDefinition (
                	name: "''' + rasterName + '''",
                	outputGranuleExtentFlag: false,
                	outputSamplingGridType: UTM,
                	rasterResolution: 100,
                	utmZoneAdjust: 0,
                	mgrsBandAdjust: 0
                ) {
                	id
                }
            }
            '''

        response = BaseCall.Base_Post(
            url = f'{globalVars.SWODLR_baseurl}/{endpoint}',
            graphQlBody = graphQlBody,
            authorizationHeader = authorizationHeader,
            authorizationHeader_invalid = authorizationHeader_invalid,
            logging = logging
        )
        
        return response


    def DeleteRasterDefinition(
            rasterDefinitionId:str,
            authorizationHeader:bool = True,
            authorizationHeader_invalid:bool = False,
            logging:bool = True
            ) -> requests.Response:
        if logging:
            print(f'\r\nDeleting Raster Definitions "{rasterDefinitionId}"...')

        graphQlBody = '''
            mutation {
            	deleteRasterDefinition (id: "''' + rasterDefinitionId + '''")
            }
            '''

        response = BaseCall.Base_Post(
            url = f'{globalVars.SWODLR_baseurl}/{endpoint}',
            graphQlBody = graphQlBody,
            authorizationHeader = authorizationHeader,
            authorizationHeader_invalid = authorizationHeader_invalid,
            logging = logging
        )
        
        return response
    