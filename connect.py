from pexpect import pxssh
from pexpect.pxssh import ExceptionPxssh
import re
def connect(host, user, password, test_cmd='uptime'):
    """
    Connects to a linux host and returns spawn id
    host -- host ip address or alias
    user -- user name
    password -- user password
    test_cmd -- Linux command to verify the host is up, default uptime
    """
    uptime_pattern = re.compile('\d{1,2}:\d{1,2}:\d{1,2}\sup')
    spawn_id = pxssh.pxssh(options={"StrictHostKeyChecking": "no", "UserKnownHostsFile": "/dev/null"})
    try:
        spawn_id.login(host, user, password)
    except ExceptionPxssh as e:
        print "Exception is returned by connect {}".format(e)
        return 0
    spawn_id.sendline(test_cmd)
    if spawn_id.prompt():
        retVal = spawn_id.before
        for line in retVal.split('\r\n'):
            if uptime_pattern.search(line):
                isHostUp = True
                return spawn_id
    return 0

def exec_cmd(spawn_id, cmd):
    """ Return the output of cmd

    spawn_id -- spawn id returned by connect
    cmd -- command to be executed.
    """

    retVal = ''
    if not spawn_id.isalive():
        return None
    spawn_id.sendline(cmd)
    if not spawn_id.prompt():
        return None
    return spawn_id.before
