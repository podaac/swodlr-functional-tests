from API.SWODLR.basecall import BaseCall
import requests

import config.globalvariables


# File wide variables
globalVars = config.globalvariables.GlobalVariables
endpoint = "api/graphql"

class Status():
    
    def GetStatusByProductID(
            productId:str,
            authorizationHeader:bool = True,
            authorizationHeader_invalid:bool = False,
            logging:bool = True
            ) -> requests.Response:
        if logging:
            print(f'\r\nGetting Status for Product "{productId}"...')

        graphQlBody = '''
            {
                statusByProduct(product: "''' + productId + '''") {
                    id
                    state
                    timestamp
                    reason
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
    

    def GetStatusByPrevious(
            productId:str,
            limit:int = 10,
            authorizationHeader:bool = True,
            authorizationHeader_invalid:bool = False,
            logging:bool = True
            ) -> requests.Response:
        if logging:
            print(f'\r\nGetting Product details for previous...')

        graphQlBody = '''
            {
                statusByPrevious(after: "''' + productId + '''", limit: ''' + limit + ''') {
                    id
                    state
                    timestamp
                    reason
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
    