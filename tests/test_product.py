from requests import Response
from json import loads

from API.SWODLR import Product

import config.globalvariables


globalVars = config.globalvariables.GlobalVariables

class TestProduct:
    def test_Product_CreateNewProduct_200(self):
        expectedStatusCode = 200
        response:Response = Product.CreateNewProduct(
            cycleNum = 2,
            passNum = 200,
            sceneNum = 200,
            authorizationHeader = True)
        assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'
        jsonContent_Create = loads(response.text)
        productId = jsonContent_Create['data']['generateL2RasterProduct']['id']
        assert productId != "", f'Product ID is not returned! "{productId}"!'
        globalVars.SWODLR_ProductId = productId


    def test_Product_CreateNewProduct_NoAuth_401(self):
        expectedStatusCode = 401
        response:Response = Product.CreateNewProduct(
            cycleNum = 2,
            passNum = 200,
            sceneNum = 200,
            authorizationHeader = False)
        assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'
    

    def test_Product_CreateNewProduct_InvalidAuth_401(self):
        expectedStatusCode = 401
        response:Response = Product.CreateNewProduct(
            cycleNum = 2,
            passNum = 200,
            sceneNum = 200,
            authorizationHeader_invalid = True)
        assert response.status_code == expectedStatusCode, f'Response code "{response.status_code}" is not "{expectedStatusCode}"!'


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
