from API.Generic.graphqlbase import GraphQlBase
from utils import ErrorInjector

import requests

import config.globalvariables


# File wide variables
globalVars = config.globalvariables.GlobalVariables
endpoint = "api/graphql"

class Product():
    
    def GetProductsOfCurrentUser(
            pageSize:int = 10,
            pageAfterId:str = "",
            authorizationHeader:bool = True,
            authorizationHeader_invalid:bool = False,
            logging:bool = True
            ) -> requests.Response:
        if logging:
            print(f'\r\nGetting Products related to Current user...')

        graphQlBody = '''
            {
            	currentUser {
            		products(limit: ''' + str(pageSize)
        if pageAfterId != "":
            graphQlBody += f', after: "{pageAfterId}"'
        graphQlBody += ''') {
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
        
        response = GraphQlBase.Base_Post(
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
            rasterResolution:int = 100,
            utmZoneAdjust:int = 0,
            mgrsBandAdjust:int = 0,
            valueTypeError:dict = {},
            authorizationHeader:bool = True,
            authorizationHeader_invalid:bool = False,
            logging:bool = True
            ) -> requests.Response:
        if logging:
            print(f'\r\nCreating new Products...')

        cycleNumString = str(cycleNum)
        passNumString = str(passNum)
        sceneNumString = str(sceneNum)
        outputGranuleExtentFlagString = 'false'
        outputSamplingGridTypeString = 'UTM'
        rasterResolutionString = f'{rasterResolution}'
        utmZoneAdjustString = f'{utmZoneAdjust}'
        mgrsBandAdjustString = f'{mgrsBandAdjust}'
        for field in valueTypeError.keys():
            expectedType = valueTypeError[field]
            if field.lower() in ['cycle', 'cyclenum']:
                cycleNumString = ErrorInjector.ValueTypeInjector(expectedType, cycleNumString)
            elif field.lower() in ['pass', 'passnum']:
                passNumString = ErrorInjector.ValueTypeInjector(expectedType, passNumString)
            elif field.lower() in ['scene', 'scenenum']:
                sceneNumString = ErrorInjector.ValueTypeInjector(expectedType, sceneNumString)
            elif field.lower() in ['outputgranuleextentflag', 'ogef']:
                outputGranuleExtentFlagString = ErrorInjector.ValueTypeInjector(expectedType, outputGranuleExtentFlagString)
            elif field.lower() in ['outputsamplinggridtype', 'osgt']:
                outputSamplingGridTypeString = ErrorInjector.ValueTypeInjector(expectedType, outputSamplingGridTypeString)
            elif field.lower() in ['rasterresolution']:
                rasterResolutionString = ErrorInjector.ValueTypeInjector(expectedType, rasterResolutionString)
            elif field.lower() in ['utmzoneadjust', 'utmza']:
                utmZoneAdjustString = ErrorInjector.ValueTypeInjector(expectedType, utmZoneAdjustString)
            elif field.lower() in ['mgrsbandadjust', 'mba']:
                mgrsBandAdjustString = ErrorInjector.ValueTypeInjector(expectedType, mgrsBandAdjustString)

        graphQlBody = '''
            mutation {
            	generateL2RasterProduct (
            		cycle: ''' + cycleNumString + ''',
            		pass: ''' + passNumString + ''',
            		scene: ''' + sceneNumString + ''',
            		outputGranuleExtentFlag: ''' + outputGranuleExtentFlagString + ''',
                	outputSamplingGridType: ''' + outputSamplingGridTypeString + ''',
                	rasterResolution: ''' + rasterResolutionString + ''',
                	utmZoneAdjust: ''' + utmZoneAdjustString + ''',
                	mgrsBandAdjust: ''' + mgrsBandAdjustString + '''
            	) {
            		id
            		status {id, state}
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