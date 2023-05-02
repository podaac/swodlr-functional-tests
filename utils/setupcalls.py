import subprocess, os, sys


class SetupCalls():

    def SetUpLogging():
        print(f"\r\nSetting up file logging...")
        tee = subprocess.Popen(["tee", "log_LatestRun.txt"], stdin=subprocess.PIPE)
        # Cause tee's stdin to get a copy of our stdin/stdout (as well as that
        # of any child processes we spawn)
        os.dup2(tee.stdin.fileno(), sys.stdout.fileno())
        os.dup2(tee.stdin.fileno(), sys.stderr.fileno())
