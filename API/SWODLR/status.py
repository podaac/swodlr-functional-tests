from API.Generic.graphqlbase import GraphQlBase
from utils import ErrorInjector

import requests

import config.globalvariables


# File wide variables
globalVars = config.globalvariables.GlobalVariables
endpoint = "api/graphql"

class Status():
    
    def GetStatusByProductID(
            productId:str,
            pageSize:int = 10,
            pageAfterId:str = "",
            valueTypeError:dict = {},
            authorizationHeader:bool = True,
            authorizationHeader_invalid:bool = False,
            logging:bool = True
            ) -> requests.Response:
        if logging:
            print(f'\r\nGetting Status for Product "{productId}"...')

        productIdString = f'"{productId}"'
        limitString = str(pageSize)
        for field in valueTypeError.keys():
            expectedType = valueTypeError[field]
            if field.lower() in ['product', 'productid']:
                productIdString = ErrorInjector.ValueTypeInjector(expectedType, productId)
            elif field.lower() == 'limit':
                limitString = ErrorInjector.ValueTypeInjector(expectedType, limitString)
        graphQlBody = '''
            {
                statusByProduct(product: ''' + productIdString + ''', limit: ''' + limitString
        if pageAfterId != "":
            graphQlBody += f', after: "{pageAfterId}"'
        graphQlBody += ''') {
                    id
                    state
                    timestamp
                    reason
                }
            }
            '''
        
        response = GraphQlBase.Base_Post(
            url = f'{globalVars.SWODLR_baseurl}/{endpoint}',
            graphQlBody = graphQlBody,
            authorizationHeader = authorizationHeader,
            authorizationHeader_invalid = authorizationHeader_invalid,
            logging = logging
        )
        
        return response
    

    def GetStatusByPrevious(
            pageAfterId:str,
            pageSize:int = 10,
            valueTypeError:dict = {},
            authorizationHeader:bool = True,
            authorizationHeader_invalid:bool = False,
            logging:bool = True
            ) -> requests.Response:
        if logging:
            print(f'\r\nGetting Product details for previous...')

        statusIdString = f'"{pageAfterId}"'
        limitString = str(pageSize)
        for field in valueTypeError.keys():
            expectedType = valueTypeError[field]
            if field.lower() in ['statusid', 'after', 'pageafterid']:
                statusIdString = ErrorInjector.ValueTypeInjector(expectedType, pageAfterId)
            elif field.lower() in ['limit', 'pagesize']:
                limitString = ErrorInjector.ValueTypeInjector(expectedType, limitString)
        
        graphQlBody = '''
            {
                statusByPrevious(after: ''' + statusIdString + ''', limit: ''' + limitString + ''') {
                    id
                    state
                    timestamp
                    reason
                }
            }
            '''
        
        response = GraphQlBase.Base_Post(
            url = f'{globalVars.SWODLR_baseurl}/{endpoint}',
            graphQlBody = graphQlBody,
            authorizationHeader = authorizationHeader,
            authorizationHeader_invalid = authorizationHeader_invalid,
            logging = logging
        )
        
        return response
    