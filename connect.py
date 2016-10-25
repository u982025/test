from pexpect import pxssh
def connect(host, user, password, test_cmd='uptime'):
    connId = pxssh.pxssh(options={"StrictHostKeyChecking": "no",  "UserKnownHostsFile": "/dev/null"})
    try: 
        spawnId.login(host, user, password): 
    except ExceptionPxssh:
        return 0
    finally:
        spawnId.sendline(test_cmd)
        if spawnId.prompt():
            retVal = spawnId.before
            for line in retVal.split('\r\n'):
                if 
