import argparse
import pytest

from config.configManager import ConfigManager
from utils.enum import Environment
from utils.edltokenhandler import EDLTokenHandler
from utils import SetupCalls

def parse_args():
    """
    Parses the program arguments
    Returns
    -------
    args
    """

    parser = argparse.ArgumentParser(
        description='Input arguments',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('-e', '--env',
                        help='Environment used to check API of.',
                        required=True,
                        choices=["uat", "ops", "sit", "ngap_uat", "ngap_ops", "ngap_sit"],
                        metavar='ops, uat, sit')

    parser.add_argument('-u', '--username',
                        help='EDL Username',
                        required=True,
                        metavar='')
    
    parser.add_argument('-pw', '--password',
                        help='EDL password',
                        required=True,
                        metavar='')
    
    args = parser.parse_args()
    return args

def run():
    """
    Run from command line.

    Returns
    -------
    """

    _args = parse_args()
    environment = Environment.from_str(_args.env)
    username = _args.username
    pw = _args.password

    SetupCalls.SetUpLogging()
    ConfigManager.InitializeConfig(
        env = environment,
        edl_Username = username,
        edl_Password = pw)
    EDLTokenHandler.GetEDLAccessToken()
    pytest.main(["tests", "--junitxml=./test-results/report.xml"])
    

if __name__ == '__main__':
    run()
