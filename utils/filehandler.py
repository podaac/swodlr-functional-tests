from time import sleep
from os import path

import json


class FileHandler():

    def WaitForFileToAppear(fileLocation:str, timeout:int=10, logging:bool=True, realPath:bool=True):
        if logging:
            print(f"\r\nWaiting for file '{fileLocation}' to appear...")
        retries = 0
        waitTime = 1
        fileLocation_rel = path.realpath(fileLocation) if realPath else fileLocation
        while retries < timeout/waitTime:
            if path.exists(fileLocation_rel):
                if logging:
                    print(f"File exists!")
                return
            elif path.islink(fileLocation_rel):
                if logging:
                    print(f"Link exists!")
                return
            else:
                sleep(waitTime)
                retries +=1
        if logging:
            print(f"File failed to appear!")


    def GetJsonFileContent(fileName:str, location:str, logging:bool=True, realPath:bool=True):
        if not fileName.endswith('.json'):
            fileName += ".json"
        if not location.endswith('/') and location != "":
            location += '/'

        fileLocation = f"{location}{fileName}"
        FileHandler.WaitForFileToAppear(fileLocation, logging = logging, realPath = realPath)
        fileContent = FileHandler.GetFileContent(fileLocation, realPath = realPath, logging = logging)
        startOfJsonIndex = fileContent.index('{')
        endOfJsonIndex = fileContent.rindex('}')
        cutContent = fileContent[startOfJsonIndex: endOfJsonIndex+1]
        data = json.loads(cutContent)
        return data


    def GetFileContent(fileLocation:str, realPath:bool=True, logging:bool=True):
        fileLocation_Real = path.realpath(fileLocation) if realPath else fileLocation
        if path.exists(fileLocation_Real):
            if logging:
                print(f'Reading file: {fileLocation_Real}')
            result = open(fileLocation_Real).read()
            return result
        elif path.islink(fileLocation_Real):
            if logging:
                print(f'Reading file: {path.realpath(fileLocation)}')
            result = open(path.realpath(fileLocation)).read()
            return result
        else:
            raise FileExistsError(f"{fileLocation_Real} does not exists!")
