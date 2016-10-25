from pexpect import pxssh
def connect(host, user, password, test_cmd='uptime'):
    """
    Connects to a linux host and returns spawn id
    """
    uptimePattern = re.compile('\d{1,2}:\d{1,2}:\d{1,2}\sup\s+\d{1,2}\smin')
    spawnId = pxssh.pxssh(options={"StrictHostKeyChecking": "no",  "UserKnownHostsFile": "/dev/null"})
    try: 
        spawnId.login(host, user, password)
    except ExceptionPxssh:
        return 0
    finally:
        spawnId.sendline(test_cmd)
        if spawnId.prompt():
            retVal = spawnId.before
            for line in retVal.split('\r\n'):
                if uptimePattern.search(line):
                    isHostUp = True
                    return spawnId
    return 0
 

def exec_cmd(spawn_id, cmd):
    """
    Executes command on a Linux host and return the output
    """
    retVal = ''
    if not spawn_id.isalive():
        return None
    spawn_id.sendline(cmd)
    if not spawn_id.prompt():
        return None
    return spawn_id.before 
