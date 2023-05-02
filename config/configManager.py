from utils.enum import Environment
from utils.filehandler import FileHandler

import config.globalvariables


# File wide variables
globVar = config.globalvariables.GlobalVariables

class ConfigManager():

    def InitializeConfig(
        env:Environment,
        edl_Username:str,
        edl_Password:str
        ):
        
        print(f"\r\nSetting config file variables...")

        envVariableJson = FileHandler.GetJsonFileContent("env.json", "./config")

        # Global
        globVar.Environment = env

        #SWODLR
        globVar.SWODLR_baseurl = envVariableJson[env.name]['SWODLR_API_BASEURL']

        # Earthdata Login
        globVar.EDL_baseurl = envVariableJson[env.name]['EARTHDATALOGIN_API_BASEURL']
        globVar.EDL_Username = edl_Username
        globVar.EDL_Password = edl_Password

