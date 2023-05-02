from utils.enum import Environment
from utils.filehandler import FileHandler

import config


# File wide variables
conf = config.config.Config

class ConfigManager():

    def InitializeConfig(
        env:Environment,
        edl_Username:str,
        edl_Password:str
        ):
        
        print(f"\r\nSetting config file variables...")

        envVariableJson = FileHandler.GetJsonFileContent("env.json", "./config")

        # Global
        conf.Environment = env

        #SWODLR
        conf.SWODLR_baseurl = envVariableJson[env.name]['SWODLR_API_BASEURL']

        # Earthdata Login
        conf.EDL_baseurl = envVariableJson[env.name]['EARTHDATALOGIN_API_BASEURL']
        conf.EDL_Username = edl_Username
        conf.EDL_Password = edl_Password

