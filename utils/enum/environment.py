from enum import Enum

class Environment(Enum):
    OPS = 1
    UAT = 2
    SIT = 3

    @staticmethod
    def from_str(env):
        if env.lower() in ["uat", "ngap_uat"]:
            return Environment.UAT
        elif env.lower() in ["ops", "ngap_ops"]:
            return Environment.OPS
        elif env.lower() in ["sit", "ngap_sit"]:
            return Environment.SIT
        else:
            NotImplemented
    