from API.SWODLR.basecall import BaseCall
import requests

import config.globalvariables


# File wide variables
globalVars = config.globalvariables.GlobalVariables
endpoint = "api/graphql"

class User():
    
    def GetCurrentUser(
            authorizationHeader:bool = True,
            authorizationHeader_invalid:bool = False,
            logging:bool = True
            ) -> requests.Response:
        if logging:
            print(f'\r\nGetting Current user...')

        graphQlBody = '''
            {
                currentUser {
                    id
		            firstName
		            lastName
		            email
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
    

    def GetCurrentUserFullDetails(
            authorizationHeader:bool = True,
            authorizationHeader_invalid:bool = False,
            logging:bool = True
            ) -> requests.Response:
        if logging:
            print(f'\r\nGetting Current user full details...')

        graphQlBody = '''
            {
                currentUser {
                    id
		            firstName
		            lastName
		            email
                    rasterDefinitions {
		            	name
		            	id
		            	outputSamplingGridType
		            	rasterResolution
		            	outputGranuleExtentFlag
		            	mgrsBandAdjust
		            	utmZoneAdjust
		            }
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
            logging = logging)
        
        return response