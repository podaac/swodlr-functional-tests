from API.SWODLR.basecall import BaseCall

import requests
import json

import config.globalvariables


# File wide variables
globalVars = config.globalvariables.GlobalVariables
endpoint = "api/graphql"

class Product():
    
    def GetProductsOfCurrentUser(
            authorizationHeader:bool = True,
            authorizationHeader_invalid:bool = False,
            logging:bool = True
            ) -> requests.Response:
        if logging:
            print(f'\r\nGetting Products related to Current user...')

        graphQlBody = '''
            {
            	currentUser {
            		products {
            			id
            			cycle
            			pass
            			scene
            			outputSamplingGridType
            			rasterResolution
            			outputGranuleExtentFlag
            			mgrsBandAdjust
            			utmZoneAdjust
            			granules {
            				id
            				timestamp
            				uri
            			}
            			status {
            				id
            				state
            				reason
            				timestamp
            			}
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
    

    def CreateNewProduct(
            cycleNum:int,
            passNum:int,
            sceneNum:int,
            authorizationHeader:bool = True,
            authorizationHeader_invalid:bool = False,
            logging:bool = True
            ) -> requests.Response:
        if logging:
            print(f'\r\nCreating new Products...')

        graphQlBody = '''
            mutation {
            	generateL2RasterProduct (
            		cycle: ''' + str(cycleNum) + ''',
            		pass: ''' + str(passNum) + ''',
            		scene: ''' + str(sceneNum) + ''',
            		outputGranuleExtentFlag: false,
                	outputSamplingGridType: UTM,
                	rasterResolution: 100,
                	utmZoneAdjust: 0,
                	mgrsBandAdjust: 0
            	) {
            		id
            		status {id, state}
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