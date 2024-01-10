from utils.enum import Environment
from utils.filehandler import FileHandler

import config.globalvariables


# File wide variables
globalVars = config.globalvariables.GlobalVariables

class ConfigManager():

    def InitializeConfig(
        env:Environment,
        edl_Username:str,
        edl_Password:str
        ):
        
        print(f"\r\nSetting config file variables...")

        envVariableJson = FileHandler.GetJsonFileContent("env.json", "./config")

        # Global
        globalVars.Environment = env

        #SWODLR
        globalVars.SWODLR_baseurl = envVariableJson[env.name]['SWODLR_API_BASEURL']

        # Earthdata Login
        globalVars.EDL_baseurl = envVariableJson[env.name]['EARTHDATALOGIN_API_BASEURL']
        globalVars.EDL_Username = edl_Username
        globalVars.EDL_Password = edl_Password

