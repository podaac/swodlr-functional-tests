from API.Generic.graphqlbase import GraphQlBase
from utils import ErrorInjector

import requests

import config.globalvariables


# File wide variables
globalVars = config.globalvariables.GlobalVariables
endpoint = "api/graphql"

class RasterDefinition():
    
    def GetRasterDefintionsOfCurrentUser(
            id: str = "",
            outputGranuleExtentFlag:bool = "null",
            outputSamplingGridType:str = "null",
            rasterResolution:int = "null",
            utmZoneAdjust:int = "null",
            mgrsBandAdjust:int = "null",
            authorizationHeader:bool = True,
            authorizationHeader_invalid:bool = False,
            logging:bool = True
            ) -> requests.Response:
        if logging:
            print(f'\r\nGetting Raster Definitions related to Current user...')
        outputGranuleExtentFlagString = str(outputGranuleExtentFlag).lower()
        graphQlBody = '''
            {
            	currentUser {
            		rasterDefinitions(
                        id:''' + f'"{id}", \
                        outputGranuleExtentFlag: {outputGranuleExtentFlagString}, \
                        outputSamplingGridType: {outputSamplingGridType}, \
                        rasterResolution: {rasterResolution}, \
                        utmZoneAdjust: {utmZoneAdjust}, \
                        mgrsBandAdjust: {mgrsBandAdjust}' + ''')
                    {
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
        
        response = GraphQlBase.Base_Post(
            url = f'{globalVars.SWODLR_baseurl}/{endpoint}',
            graphQlBody = graphQlBody,
            authorizationHeader = authorizationHeader,
            authorizationHeader_invalid = authorizationHeader_invalid,
            logging = logging
        )
        
        return response


    def CreateNewRasterDefinition(
            rasterName:str,
            rasterResolution:int = 100,
            utmZoneAdjust:int = 0,
            mgrsBandAdjust:int = 0,
            valueTypeError:dict = {},
            authorizationHeader:bool = True,
            authorizationHeader_invalid:bool = False,
            logging:bool = True
            ) -> requests.Response:
        if logging:
            print(f'\r\nCreating a new Raster Definition related to Current user...')

        rasterNameString = f'"{rasterName}"'
        outputGranuleExtentFlagString = 'false'
        outputSamplingGridTypeString = 'UTM'
        rasterResolutionString = f'{rasterResolution}'
        utmZoneAdjustString = f'{utmZoneAdjust}'
        mgrsBandAdjustString = f'{mgrsBandAdjust}'
        for field in valueTypeError.keys():
            expectedType = valueTypeError[field]
            if field.lower() in ['rastername', 'name']:
                rasterNameString = ErrorInjector.ValueTypeInjector(expectedType, rasterName)
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
                createRasterDefinition (
                	name: ''' + rasterNameString + ''',
                	outputGranuleExtentFlag: ''' + outputGranuleExtentFlagString + ''',
                	outputSamplingGridType: ''' + outputSamplingGridTypeString + ''',
                	rasterResolution: ''' + rasterResolutionString + ''',
                	utmZoneAdjust: ''' + utmZoneAdjustString + ''',
                	mgrsBandAdjust: ''' + mgrsBandAdjustString + '''
                ) {
                	id
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


    def DeleteRasterDefinition(
            rasterDefinitionId:str,
            valueTypeError:dict = {},
            authorizationHeader:bool = True,
            authorizationHeader_invalid:bool = False,
            logging:bool = True
            ) -> requests.Response:
        if logging:
            print(f'\r\nDeleting Raster Definitions "{rasterDefinitionId}"...')

        rasterDefinitionIdString = f'"{rasterDefinitionId}"'
        for field in valueTypeError.keys():
            expectedType = valueTypeError[field]
            if field.lower() in ['rasterdefinition', 'rasterdefinitionid', 'id']:
                rasterDefinitionIdString = ErrorInjector.ValueTypeInjector(expectedType, rasterDefinitionId)

        graphQlBody = '''
            mutation {
            	deleteRasterDefinition (id: ''' + rasterDefinitionIdString + ''')
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
    