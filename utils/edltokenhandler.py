from datetime import datetime

import json
import subprocess, os, sys

from API.EDL import Token

import config.globalvariables


globVar = config.globalvariables.GlobalVariables

class EDLTokenHandler():

    def SetUpLogging():
        print(f"\r\nSetting up file logging...")
        tee = subprocess.Popen(["tee", "log_LatestRun.txt"], stdin=subprocess.PIPE)
        # Cause tee's stdin to get a copy of our stdin/stdout (as well as that
        # of any child processes we spawn)
        os.dup2(tee.stdin.fileno(), sys.stdout.fileno())
        os.dup2(tee.stdin.fileno(), sys.stderr.fileno())


    def GetEDLAccessToken():
        print(f"\r\nGet EDL Access Token - Started")
        response = Token.GetExistingToken()
        if response.status_code != 200:
            print("Getting existing access token - FAILED")
            print("Requesting new access token!")
            response = EDLTokenHandler.GetNewToken()
        elif response.text == "[]":
            print("No access token exists for the user!")
            print("Requesting new access token!")
            response = EDLTokenHandler.GetNewToken()
        if response != None:
            data = ""
            if response.text.startswith('['):
                data = json.loads(response.text)[0]
            else:
                data = json.loads(response.text)
            date = datetime.today().strftime("%m/%d/%Y")
            print("Access Token found!")
            if data["expiration_date"] == date:
                print("Access Token expires today!")
                print("Deleting expiring access token!")
                Token.DeleteExistingToken(data["access_token"])
                print("Requesting new access token!")
                response = EDLTokenHandler.GetNewToken()
                data = json.loads(response.text)[0]
            access_token = data["access_token"]
            print("Saving access token!")
            globVar.EDL_AccessToken = access_token
        print("Get Access EDL Token - Finished")


    def GetNewToken():
        response = Token.RequestNewToken()
        if response.status_code == 200 and response.text != "[]":
            print("Getting new Access Token - SUCCESS")
            return response
        else:
            print("Getting new Access Token - FAILED")
            print(f"Reason: {json.loads(response.text)['error_description']}")
            raise PermissionError(f"Reason: {json.loads(response.text)['error_description']}")
