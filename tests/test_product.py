from requests import Response
from json import loads

from API.SWODLR import Product
from utils import Verifications

import config.globalvariables


globalVars = config.globalvariables.GlobalVariables

class TestProduct:

# ========================================== generateL2RasterProduct ==========================================

    def test_Product_CreateNewProduct_200(self):
        expectedStatusCode = 200
        response:Response = Product.CreateNewProduct(
            cycleNum = 0,
            passNum = 0,
            sceneNum = 0)
        assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'
        jsonContent_Create = loads(response.text)
        productId = jsonContent_Create['data']['generateL2RasterProduct']['id']
        assert productId != "", f'Product ID is not returned! "{productId}"!'
        globalVars.SWODLR_ProductId = productId


    def test_Product_CreateNewProduct_NoAuth_401(self):
        expectedStatusCode = 401
        response:Response = Product.CreateNewProduct(
            cycleNum = 0,
            passNum = 0,
            sceneNum = 0,
            authorizationHeader = False)
        assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'
    

    def test_Product_CreateNewProduct_InvalidAuth_401(self):
        expectedStatusCode = 401
        response:Response = Product.CreateNewProduct(
            cycleNum = 0,
            passNum = 0,
            sceneNum = 0,
            authorizationHeader_invalid = True)
        assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'


    def test_Product_CreateNewProduct_Value_Wrong_Cycle_Negative(self):
        response:Response = Product.CreateNewProduct(
            cycleNum = -1,
            passNum = 0,
            sceneNum = 0)
        expectedStatusCode = 200
        expectedError = "must be >= 0 and < 1000"
        expectedType = "ValidationError"
        Verifications.ErrorVerification(
            response = response,
            fieldName = "N/A",
            expectedStatusCode = expectedStatusCode,
            expectedError = expectedError,
            expectedType = expectedType,
            checkForData = False
        )


    def test_Product_CreateNewProduct_Value_Wrong_Cycle_MaxLimit(self):
        response:Response = Product.CreateNewProduct(
            cycleNum = 1000,
            passNum = 0,
            sceneNum = 0)
        expectedStatusCode = 200
        expectedError = "must be >= 0 and < 1000"
        expectedType = "ValidationError"
        Verifications.ErrorVerification(
            response = response,
            fieldName = "N/A",
            expectedStatusCode = expectedStatusCode,
            expectedError = expectedError,
            expectedType = expectedType,
            checkForData = False
        )

    
    def test_Product_CreateNewProduct_Type_Wrong_Cycle(self):
        response:Response = Product.CreateNewProduct(
            cycleNum = 0,
            passNum = 0,
            sceneNum = 0,
            valueTypeError = {'cycle':'string'})
        expectedStatusCode = 200
        expectedError = "validation error of type wrongtype: argument 'cycle' with value 'stringvalue"
        expectedType = "ValidationError"
        Verifications.ErrorVerification(
            response = response,
            fieldName = "N/A",
            expectedStatusCode = expectedStatusCode,
            expectedError = expectedError,
            expectedType = expectedType,
            checkForData = False
        )

    
    def test_Product_CreateNewProduct_Value_Wrong_Pass_Negative(self):
        response:Response = Product.CreateNewProduct(
            cycleNum = 0,
            passNum = -1,
            sceneNum = 0)
        expectedStatusCode = 200
        expectedError = "must be >= 0 and < 1000"
        expectedType = "ValidationError"
        Verifications.ErrorVerification(
            response = response,
            fieldName = "N/A",
            expectedStatusCode = expectedStatusCode,
            expectedError = expectedError,
            expectedType = expectedType,
            checkForData = False
        )


    def test_Product_CreateNewProduct_Value_Wrong_Pass_MaxLimit(self):
        response:Response = Product.CreateNewProduct(
            cycleNum = 0,
            passNum = 1000,
            sceneNum = 0)
        expectedStatusCode = 200
        expectedError = "must be >= 0 and < 1000"
        expectedType = "ValidationError"
        Verifications.ErrorVerification(
            response = response,
            fieldName = "N/A",
            expectedStatusCode = expectedStatusCode,
            expectedError = expectedError,
            expectedType = expectedType,
            checkForData = False
        )

    
    def test_Product_CreateNewProduct_Type_Wrong_Pass(self):
        response:Response = Product.CreateNewProduct(
            cycleNum = 0,
            passNum = 0,
            sceneNum = 0,
            valueTypeError = {'pass':'string'})
        expectedStatusCode = 200
        expectedError = "validation error of type wrongtype: argument 'pass' with value 'stringvalue"
        expectedType = "ValidationError"
        Verifications.ErrorVerification(
            response = response,
            fieldName = "N/A",
            expectedStatusCode = expectedStatusCode,
            expectedError = expectedError,
            expectedType = expectedType,
            checkForData = False
        )


    def test_Product_CreateNewProduct_Value_Wrong_Scene_Negative(self):
        response:Response = Product.CreateNewProduct(
            cycleNum = 0,
            passNum = 0,
            sceneNum = -1)
        expectedStatusCode = 200
        expectedError = "must be >= 0 and < 1000"
        expectedType = "ValidationError"
        Verifications.ErrorVerification(
            response = response,
            fieldName = "N/A",
            expectedStatusCode = expectedStatusCode,
            expectedError = expectedError,
            expectedType = expectedType,
            checkForData = False
        )


    def test_Product_CreateNewProduct_Value_Wrong_Scene_MaxLimit(self):
        response:Response = Product.CreateNewProduct(
            cycleNum = 0,
            passNum = 0,
            sceneNum = 1000)
        expectedStatusCode = 200
        expectedError = "must be >= 0 and < 1000"
        expectedType = "ValidationError"
        Verifications.ErrorVerification(
            response = response,
            fieldName = "N/A",
            expectedStatusCode = expectedStatusCode,
            expectedError = expectedError,
            expectedType = expectedType,
            checkForData = False
        )

    
    def test_Product_CreateNewProduct_Type_Wrong_Scene(self):
        response:Response = Product.CreateNewProduct(
            cycleNum = 0,
            passNum = 0,
            sceneNum = 0,
            valueTypeError = {'scene':'string'})
        expectedStatusCode = 200
        expectedError = "validation error of type wrongtype: argument 'scene' with value 'stringvalue"
        expectedType = "ValidationError"
        Verifications.ErrorVerification(
            response = response,
            fieldName = "N/A",
            expectedStatusCode = expectedStatusCode,
            expectedError = expectedError,
            expectedType = expectedType,
            checkForData = False
        )

    
    def test_Product_CreateNewProduct_Type_Wrong_OutputGranuleExtentFlag(self):
        response:Response = Product.CreateNewProduct(
            cycleNum = 0,
            passNum = 0,
            sceneNum = 0,
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

    
    def test_Product_CreateNewProduct_Type_Wrong_OutputSamplingGridType(self):
        response:Response = Product.CreateNewProduct(
            cycleNum = 0,
            passNum = 0,
            sceneNum = 0,
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
    

    def test_Product_CreateNewProduct_Value_Wrong_RasterResolution_Negative(self):
        response:Response = Product.CreateNewProduct(
            cycleNum = 0,
            passNum = 0,
            sceneNum = 0,
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

    
    def test_Product_CreateNewProduct_Value_Wrong_RasterResolution_MaxLimit(self):
        response:Response = Product.CreateNewProduct(
            cycleNum = 0,
            passNum = 0,
            sceneNum = 0,
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


    def test_Product_CreateNewProduct_Type_Wrong_RasterResolution_String(self):
        response:Response = Product.CreateNewProduct(
            cycleNum = 0,
            passNum = 0,
            sceneNum = 0,
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


    def test_Product_CreateNewProduct_Value_Wrong_UtmZoneAdjust_Negative(self):
        response:Response = Product.CreateNewProduct(
            cycleNum = 0,
            passNum = 0,
            sceneNum = 0,
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


    def test_Product_CreateNewProduct_Value_Wrong_UtmZoneAdjust_MaxLimit(self):
        response:Response = Product.CreateNewProduct(
            cycleNum = 0,
            passNum = 0,
            sceneNum = 0,
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

    
    def test_Product_CreateNewProduct_Type_Wrong_UtmZoneAdjust(self):
        response:Response = Product.CreateNewProduct(
            cycleNum = 0,
            passNum = 0,
            sceneNum = 0,
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


    def test_Product_CreateNewProduct_Value_Wrong_MgrsBandAdjust_Negative(self):
        response:Response = Product.CreateNewProduct(
            cycleNum = 0,
            passNum = 0,
            sceneNum = 0,
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


    def test_Product_CreateNewProduct_Value_Wrong_MgrsBandAdjust_MaxLimit(self):
        response:Response = Product.CreateNewProduct(
            cycleNum = 0,
            passNum = 0,
            sceneNum = 0,
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

    
    def test_Product_CreateNewProduct_Type_Wrong_MgrsBandAdjust(self):
        response:Response = Product.CreateNewProduct(
            cycleNum = 0,
            passNum = 0,
            sceneNum = 0,
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


# ========================================== currentUser ==========================================

    def test_Product_GetProductsOfCurrentUser_200(self):
        expectedStatusCode = 200
        response:Response = Product.GetProductsOfCurrentUser(authorizationHeader = True)
        assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'
        productId = globalVars.SWODLR_ProductId
        jsonContent = loads(response.text)
        products = jsonContent['data']['currentUser']['products']
        found = False
        for product in products:
            if product['id'] == productId:
                found = True
        assert found, f'Previously created product "{productId}" is not among current user\'s products: "{products}"'


    def test_Product_GetProductsOfCurrentUser_NoAuth_401(self):
        expectedStatusCode = 401
        response:Response = Product.GetProductsOfCurrentUser(authorizationHeader = False)
        assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'
    

    def test_Product_GetProductsOfCurrentUser_InvalidAuth_401(self):
        expectedStatusCode = 401
        response:Response = Product.GetProductsOfCurrentUser(authorizationHeader_invalid = True)
        assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'


    def test_Product_GetProductsOfCurrentUser_Pagination(self):
        expectedStatusCode = 200
        pageSize = 3
        response:Response = Product.GetProductsOfCurrentUser(pageSize = pageSize)
        assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'
        count = -1
        page = 0
        while count != 0:
            jsonContent = loads(response.text)
            products = jsonContent['data']['currentUser']['products']
            count = len(products)
            print(products)
            print(f'Count: {count}')
            if len(products) == pageSize:                
                lastId = products[count-1]['id']
                print(f'LastId: {lastId}')
                response:Response = Product.GetProductsOfCurrentUser(pageSize = pageSize, pageAfterId = lastId)
                assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'
                page += 1
            else:
                count = 0
        assert page > 0, f'No pagination happened!' 
            